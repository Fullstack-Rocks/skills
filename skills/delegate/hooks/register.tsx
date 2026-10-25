import { atom, read } from 'claude-code'
import type { EngineInterface, Register } from 'claude-code'

import type {
  Brand,
  DelegateEvent,
  Delegation,
  Fold,
  ModelOption,
  NavAction,
  NavProps,
  QueuedMessage,
} from '../types'

// Panes drawn from what scripts/delegate.py writes under <project>/.delegate/. Delegations (LIST) is
// the chat list by project (hooks/nav.tsx), pinned: the person's close is refused. Clicking a chat
// opens it in a tab of its own (chat-<id>), one document the surface scrolls itself: the chat's
// header, its whole conversation, then the composer. Nothing floats over the conversation, so
// nothing has to follow the scroll.

const LIST = 'delegate'
const LIST_TITLE = '☰ Delegations'
const CHAT = 'chat-' // a chat's pane id is CHAT + its delegation id
const ARCHIVE = 'delegate-archive'
const NO_PROJECT = '__none'
const NEW_PROJECT = '__new'
const DEFAULT = 'default'
const SELECT_MAX = 64
// The engine draws 100,000 characters of a tree (texts, labels, logos' sources), and past that drops
// elements, which the desktop refuses whole, keeping the last tree it took. So a conversation draws its
// newest DRAWN_CHARS, the rest of the pane well inside the remainder. Long thinking and tool output start
// folded (output to its first PREVIEW lines), so a chat usually fits whole and the surface scrolls it
// from its first message. One that doesn't fit draws the next older batch (EARLIER more) when scrolled to
// the top, its newest rows giving way, and scrolling to the bottom brings them back.
const DRAWN_CHARS = 60_000
const EARLIER = 20_000
const LONG = 12 // lines of thinking or tool output past which it starts folded
const PREVIEW = 3
// A working chat's tab turns a spinner, one frame per SPIN_MS (nav.tsx turns its own in the list).
const SPINNER = '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'
const SPIN_MS = 250

// Helpers write state through $.state with these refs; the render hooks read the atoms over them.
const DELEGATIONS = { plugin: 'delegate', key: 'delegations' } as const
const SELECTED = { plugin: 'delegate', key: 'selected' } as const
const PAGE = { plugin: 'delegate', key: 'page' } as const
const SENDING = { plugin: 'delegate', key: 'sending' } as const
const MODELS = { plugin: 'delegate', key: 'models' } as const
const NAMING = { plugin: 'delegate', key: 'naming' } as const
const DRAFTS = { plugin: 'delegate', key: 'drafts' } as const
const ATTACHMENTS = { plugin: 'delegate', key: 'attachments' } as const
const QUEUE = { plugin: 'delegate', key: 'queue' } as const
const EXTRA = { plugin: 'delegate', key: 'extra' } as const
const FOLDS = { plugin: 'delegate', key: 'folds' } as const
const delegations = atom(DELEGATIONS, [])
// The chat opened last, lit in the list.
const selected = atom(SELECTED, '')
// A revision of the open chats' events (they live in eventsOf): a change redraws.
const page = atom(PAGE, { start: 0, end: 0, total: 0 })
const sending = atom(SENDING, '')
const models = atom(MODELS, {})
// The chat whose project is being named in a new-project field, '' for none.
const naming = atom(NAMING, '')
// Per chat: the unsent message and the paths attached to it.
const drafts = atom(DRAFTS, {})
const attachments = atom(ATTACHMENTS, {})
// Per chat: messages queued behind its running turn.
const queue = atom(QUEUE, {})
// Per chat: characters of older conversation drawn beyond DRAWN_CHARS, grown by scrolling to the top.
const earlier = atom(EXTRA, {})
// Per chat: whether its thinking is hidden, and the blocks folded or unfolded against that.
const folds = atom(FOLDS, {})

// Names, colours, glyphs and SVG logos, from assets/brands.json (shared with the script and the MCP App).
let brands: Record<string, Brand> = {}
const brandOf = (who: string): Brand =>
  brands[who] ?? brands.lead ?? { name: who, color: '#8A8A8A', glyph: '◆', svg: '' }

// File path -> mtime at the last read. Module state, so a reload re-reads everything once.
const stamps = new Map<string, number>()
// The read of .delegate/ in flight, which a second caller waits for.
let polling: Promise<void> | undefined
const fetchingModels = new Set<string>()
const markingSeen = new Set<string>()
// Per chat, the last finished turn the lead agent has been told about (for the person's own messages).
const reported = new Map<string, number>()
// Per open chat: every event, read from its events.jsonl.
const eventsOf = new Map<string, DelegateEvent[]>()
// Per open chat: whether its window is at the newest line (so new output keeps it there), and whether
// older or newer rows exist than the ones drawn.
const following = new Map<string, boolean>()
const edges = new Map<string, { hasEarlier: boolean; hasLater: boolean }>()
// Pane id -> the title it was last given, so a rename or a spinner frame retitles it.
const titles = new Map<string, string>()
let frame = 0

const clip = (text: string, n: number) => {
  const flat = text.replace(/\s+/g, ' ').trim()
  return flat.length <= n ? flat : `${flat.slice(0, n - 1)}…`
}

const baseName = (path: string) => path.replace(/\/+$/, '').split('/').pop() ?? path

const chatOf = (paneId: string) => (paneId.startsWith(CHAT) ? paneId.slice(CHAT.length) : '')

// A finished turn the person hasn't looked at yet.
const isUnread = (d: Delegation) => d.status !== 'running' && d.turns > 0 && d.turns > d.seenTurns

const parseLines = <T,>(text: string): T[] =>
  text
    .split('\n')
    .filter(Boolean)
    .flatMap(line => {
      try {
        return [JSON.parse(line) as T]
      } catch {
        return []
      }
    })

// A chat's events as rows at a width: a header row per event, then its whole body unless folded.
// Messages and replies are markdown, one row per block (a paragraph, a list, a fenced code block),
// drawn as Markdown; the rest is plain lines. Keys are the event's place in the log, which only grows
// (two events can share a timestamp, and a tree with a key twice is refused whole).
type Row = { key: string; ev: DelegateEvent; kind: 'head' | 'body' | 'md' | 'gap'; text: string; foldable: boolean; folded: boolean }

// Splits markdown into blocks at blank lines, keeping a fenced code block whole.
function markdownBlocks(text: string): string[] {
  const blocks: string[] = []
  let block: string[] = []
  let isFenced = false
  for (const line of text.split('\n')) {
    if (line.trimStart().startsWith('```')) isFenced = !isFenced
    if (!isFenced && !line.trim()) {
      if (block.length) blocks.push(block.join('\n'))
      block = []
      continue
    }
    block.push(line)
  }
  if (block.length) blocks.push(block.join('\n'))
  return blocks
}

function wrap(text: string, width: number): string[] {
  const out: string[] = []
  for (const raw of text.split('\n')) {
    let line = ''
    for (const word of raw.split(/(\s+)/)) {
      if (line.length + word.length <= width) {
        line += word
        continue
      }
      if (line.trim()) out.push(line.trimEnd())
      line = word.trimStart()
      while (line.length > width) {
        out.push(line.slice(0, width))
        line = line.slice(width)
      }
    }
    out.push(line.trimEnd())
  }
  return out
}

// Thinking and tool output fold; a block is folded when the chat folds its kind, or when it is long,
// unless the person unfolded that one (and the other way round).
const isFolded = (ev: DelegateEvent, key: string, lines: number, fold: Fold | undefined) =>
  ((ev.kind === 'thinking' ? fold?.hideThinking === true : fold?.hideTools === true) || lines > LONG) !==
  (fold?.toggled ?? []).includes(key)

function toRows(list: DelegateEvent[], harness: string, width: number, fold: Fold | undefined): Row[] {
  const rows: Row[] = []
  list.forEach((ev, n) => {
    const key = `e${n}`
    const body = ev.kind === 'tool' ? ev.text.split('\n').slice(1).join('\n') : ev.kind === 'status' ? '' : ev.text
    const lines = ev.kind === 'message' || ev.kind === 'final' ? [] : body.trim() ? wrap(body, width) : []
    const foldable = (ev.kind === 'thinking' || ev.kind === 'tool' || ev.kind === 'tool_result') && lines.length > 0
    const count = body.trim().split('\n').length
    const folded = foldable && isFolded(ev, key, count, fold)
    // Folded output keeps its first lines in view, as a preview; folded thinking keeps none.
    const preview = ev.kind === 'thinking' ? '' : body.trim().split('\n').slice(0, PREVIEW).join('\n')
    const shown = folded ? (preview ? wrap(preview, width) : []) : lines
    const label = {
      message: ev.from === harness ? ev.from : `${ev.from} → ${harness}`,
      final: `${ev.from} · turn ${ev.turn} · ${ev.seconds ?? 0}s · STATUS: ${ev.status ?? '?'}`,
      thinking: folded ? `thinking · ${count} lines` : 'thinking',
      tool: `› ${ev.text.split('\n')[0]}`,
      tool_result: folded ? `↳ output · ${count} lines` : '↳ output',
      error: '✗ error',
      status: `· ${ev.text}`,
    }[ev.kind]
    rows.push({ key: `${key}-h`, ev, kind: 'head', text: label, foldable, folded })
    if (ev.kind === 'message' || ev.kind === 'final') {
      const files = ev.kind === 'message' && ev.attachments?.length ? `\n\n📎 ${ev.attachments.join(', ')}` : ''
      markdownBlocks(ev.text + files).forEach((text, i) => {
        rows.push({ key: `${key}-${i}`, ev, kind: 'md', text, foldable: false, folded: false })
      })
    } else {
      shown.forEach((text, i) => rows.push({ key: `${key}-${i}`, ev, kind: 'body', text, foldable: false, folded: false }))
      if (folded && shown.length && count > PREVIEW) {
        rows.push({ key: `${key}-more`, ev, kind: 'body', text: `… ${count - PREVIEW} more lines (▸ unfolds)`, foldable: false, folded: false })
      }
    }
    if (n < list.length - 1) rows.push({ key: `${key}-gap`, ev, kind: 'gap', text: ' ', foldable: false, folded: false })
  })
  return rows
}

// Tells the render hooks the events changed; they live in eventsOf, not in state.
async function showPage($: EngineInterface) {
  const total = [...eventsOf.values()].reduce((sum, list) => sum + list.length, 0)
  const was = (await $.state.get(PAGE)).value ?? { start: 0, end: 0, total: 0 }
  await $.state.set(PAGE, { start: 0, end: was.end + 1, total })
}

async function changed($: EngineInterface, path: string) {
  const stat = await $.fs.stat(path).catch(() => undefined)
  if (!stat || stamps.get(path) === stat.mtimeMs) return false
  stamps.set(path, stat.mtimeMs)
  return true
}

function toDelegation(s: Record<string, unknown>, meta: Record<string, unknown>): Delegation {
  const title = String(s.title ?? '')
  return {
    id: String(s.id),
    harness: String(s.harness),
    status: String(s.status ?? 'idle'),
    agentStatus: String(s.agent_status ?? ''),
    mode: String(s.mode ?? 'read'),
    turns: Number(s.turns ?? 0),
    title,
    name: String(meta.name ?? '') || title || String(s.id),
    model: String(s.model ?? ''),
    effort: String(s.effort ?? ''),
    speed: String(s.speed ?? ''),
    created: Number(s.created ?? 0),
    archived: meta.archived === true,
    project: String(meta.project ?? ''),
    seenTurns: Number(meta.seen_turns ?? 0),
  }
}

async function readDelegation($: EngineInterface, folder: string) {
  const meta = await $.fs.read(`${folder}/meta.json`).then(text => JSON.parse(text), () => ({}))
  return toDelegation(JSON.parse(await $.fs.read(`${folder}/state.json`)), meta)
}

// The person wrote to a delegate from the pane: once that turn ends, the lead agent gets both sides.
async function reportUserTurns($: EngineInterface, folder: string, d: Delegation) {
  const done = d.status === 'running' ? d.turns - 1 : d.turns
  const since = reported.get(d.id)
  reported.set(d.id, done)
  if (since === undefined || done <= since) return
  const log = parseLines<DelegateEvent>(await $.fs.read(`${folder}/events.jsonl`).catch(() => ''))
  for (let turn = since + 1; turn <= done; turn++) {
    const asked = log.find(ev => ev.turn === turn && ev.kind === 'message')
    const reply = log.find(ev => ev.turn === turn && ev.kind === 'final')
    if (asked?.from !== 'user' || !reply) continue
    const text = `[delegate] The user messaged ${d.id} (${d.harness}) from the Delegate pane:\n${asked.text}\n\n${d.id} replied (STATUS: ${reply.status ?? '?'}):\n${reply.text}`
    await $.session.append({ message: { type: 'user', content: [{ type: 'text', text }] } })
  }
}

// Reads .delegate/ into state. The clock polls too, so a caller that finds a read in flight waits
// for it, and then reads what it read.
function poll($: EngineInterface) {
  polling ??= readAll($).finally(() => {
    polling = undefined
  })
  return polling
}

async function readAll($: EngineInterface) {
  const base = `${await $.session.root()}/.delegate`
  if (!(await $.fs.exists(base))) return
  const before = (await $.state.get(DELEGATIONS)).value ?? []
  const dirs = (await $.fs.list(base)).filter(entry => entry.kind === 'dir')
  let isDirty = dirs.length !== before.length
  const now: Delegation[] = []
  const started: string[] = []
  for (const dir of dirs) {
    const folder = `${base}/${dir.name}`
    const old = before.find(one => one.id === dir.name)
    // Both checks run, so both stamps stay current.
    const isStale = [await changed($, `${folder}/state.json`), await changed($, `${folder}/meta.json`)].some(Boolean)
    if (old && !isStale) {
      now.push(old)
      continue
    }
    const fresh = await readDelegation($, folder).catch(() => undefined)
    if (!fresh) continue
    now.push(fresh)
    isDirty = true
    await reportUserTurns($, folder, fresh)
    if (fresh.status === 'running' && old?.status !== 'running') started.push(fresh.id)
    if (old?.status === 'running' && fresh.status !== 'running') {
      $.ui.toast(`${brandOf(fresh.harness).glyph} ${fresh.name} replied (STATUS: ${fresh.agentStatus || '?'})`)
    }
  }
  if (isDirty) await $.state.set(DELEGATIONS, now.sort((a, b) => a.created - b.created))

  const running = now.filter(one => one.status === 'running')
  $.ui.status(running.length ? running.map(one => `${brandOf(one.harness).glyph} ${one.name} working`).join('  ') : undefined)

  // A turn that starts opens its chat in a tab, after this read (opening reads the chat in).
  for (const id of started) void openChat($, id, false)
  const panes = await $.ui.panes()
  const queues = (await $.state.get(QUEUE)).value ?? {}
  let isNewQueue = false
  let isNewEvents = false
  for (const pane of panes) {
    const chat = now.find(one => one.id === chatOf(pane.id))
    // A tab nothing draws any more (its chat deleted, or a pane id of an older version) is closed.
    if (!chat && pane.id !== LIST && pane.id !== ARCHIVE) void $.ui.close({ id: pane.id }).catch(() => undefined)
    if (!chat) continue
    void loadModels($, chat.harness)
    // A mark that fails is tried again on the next poll.
    if (isUnread(chat) && pane.isShown) void markSeen($, chat.id).catch(() => undefined)
    await retitle($, chat)
    const log = `${base}/${chat.id}/events.jsonl`
    if (await changed($, log)) {
      eventsOf.set(chat.id, parseLines<DelegateEvent>(await $.fs.read(log)))
      isNewEvents = true
      if (following.get(chat.id) !== false) $.clock.after(50, () => toEnd($, chat.id))
    }
    const queued = `${base}/${chat.id}/queue.jsonl`
    if (await changed($, queued)) {
      queues[chat.id] = parseLines<QueuedMessage>(await $.fs.read(queued))
      isNewQueue = true
    }
  }
  if (isNewEvents) await showPage($)
  if (isNewQueue) await $.state.set(QUEUE, { ...queues })
}

// A chat's tab: its spinner while it works, its agent's glyph, its name.
const titleOf = (d: Delegation) =>
  `${d.status === 'running' ? `${SPINNER[frame % SPINNER.length]} ` : ''}${brandOf(d.harness).glyph} ${clip(d.name, 40)}`

// Gives an open chat's tab its current title; opening an open id retitles it.
async function retitle($: EngineInterface, d: Delegation) {
  const title = titleOf(d)
  if (titles.get(CHAT + d.id) === title) return
  titles.set(CHAT + d.id, title)
  await $.ui.open({ id: CHAT + d.id, title })
}

// Turns the spinners of the open, working chats' tabs.
async function spin($: EngineInterface) {
  const working = ((await $.state.get(DELEGATIONS)).value ?? []).filter(one => one.status === 'running')
  if (!working.length) return
  frame++
  const open = new Set((await $.ui.panes()).map(pane => pane.id))
  for (const d of working) if (open.has(CHAT + d.id)) await retitle($, d)
}

// Shows a chat's newest line: its window goes to the end, and keeps following new output from there.
function toEnd($: EngineInterface, id: string) {
  following.set(id, true)
  if (edges.get(id)?.hasLater) void setExtra($, id, 0)
  const place = async () => {
    await $.ui.scroll({ to: 'end', in: CHAT + id })
  }
  void place().catch(() => undefined)
  $.clock.after(300, () => void place().catch(() => undefined))
}

async function setExtra($: EngineInterface, id: string, chars: number) {
  const all = (await $.state.get(EXTRA)).value ?? {}
  await $.state.set(EXTRA, { ...all, [id]: chars })
}

// Opens a chat in its own tab (or brings its open tab forward) at its newest line.
async function openChat($: EngineInterface, id: string, isAsked: boolean) {
  const chat = ((await $.state.get(DELEGATIONS)).value ?? []).find(one => one.id === id)
  if (!chat) return
  const base = `${await $.session.root()}/.delegate`
  const isOpen = (await $.ui.panes()).some(pane => pane.id === CHAT + id)
  if (!isOpen) {
    stamps.delete(`${base}/${id}/events.jsonl`)
    stamps.delete(`${base}/${id}/queue.jsonl`)
    await setExtra($, id, 0)
  }
  await $.state.set(SELECTED, id)
  const title = titleOf(chat)
  titles.set(CHAT + id, title)
  await $.ui.open({ id: CHAT + id, title, ...(isAsked ? { focus: true as const } : {}) })
  if (!isOpen) {
    await poll($)
    toEnd($, id)
  }
}

async function openArchive($: EngineInterface) {
  await $.ui.open({ id: ARCHIVE, title: '⊟ Archived', focus: true })
}

async function markSeen($: EngineInterface, id: string) {
  if (markingSeen.has(id)) return
  markingSeen.add(id)
  try {
    await run($, ['meta', id, '--seen'])
  } finally {
    markingSeen.delete(id)
  }
}

// Archive, unarchive, rename or tag a chat; the next poll reads the change back from meta.json.
async function setMeta($: EngineInterface, id: string, flags: string[]) {
  await run($, ['meta', id, ...flags])
  await poll($)
}

// What the chat list posts: a click, a menu choice, a rename.
async function onNav($: EngineInterface, action: NavAction) {
  switch (action.type) {
    case 'select':
      return action.target === '__archived' ? openArchive($) : openChat($, action.target, true)
    case 'archive':
      return setMeta($, action.target, ['--archive'])
    case 'rename':
      return setMeta($, action.target, ['--name', action.value])
    case 'rename-project':
      await run($, ['rename-project', action.target, action.value])
      return poll($)
    case 'delete':
      await $.ui.close({ id: CHAT + action.target })
      await run($, ['delete', action.target])
      return poll($)
  }
}

// Folds or unfolds one block of a chat, or hides or shows all of its thinking.
async function setFold($: EngineInterface, id: string, change: (fold: Fold) => Fold) {
  const all = (await $.state.get(FOLDS)).value ?? {}
  await $.state.set(FOLDS, { ...all, [id]: change(all[id] ?? { hideThinking: false, hideTools: false, toggled: [] }) })
}

const toggleBlock = (fold: Fold, key: string): Fold => ({
  ...fold,
  toggled: fold.toggled.includes(key) ? fold.toggled.filter(one => one !== key) : [...fold.toggled, key],
})

// Each harness's model list, asked of delegate.py once per session.
async function loadModels($: EngineInterface, harness: string) {
  const known = (await $.state.get(MODELS)).value ?? {}
  if (known[harness] || fetchingModels.has(harness)) return
  fetchingModels.add(harness)
  try {
    const script = `${$.plugin.root}/scripts/delegate.py`
    const out = await $.process.run(['python3', script, 'models', harness, '--json'], { timeoutMs: 60_000 })
    const list = out.exitCode === 0 ? (JSON.parse(out.stdout) as ModelOption[]) : []
    await $.state.set(MODELS, { ...known, [harness]: list })
  } finally {
    fetchingModels.delete(harness)
  }
}

async function choose($: EngineInterface, id: string, flag: '--model' | '--effort' | '--speed', value: string) {
  await run($, ['set', id, flag, value])
  await poll($)
}

async function setDraft($: EngineInterface, id: string, text: string) {
  const all = (await $.state.get(DRAFTS)).value ?? {}
  await $.state.set(DRAFTS, { ...all, [id]: text })
}

// The system's file dialog (Finder on macOS), through delegate.py; the chosen paths join the draft's.
async function pickFiles($: EngineInterface, id: string, folders: boolean) {
  const script = `${$.plugin.root}/scripts/delegate.py`
  const out = await $.process.run(['python3', script, 'pick', ...(folders ? ['--folders'] : [])], { timeoutMs: 600_000 })
  if (out.exitCode !== 0) {
    $.ui.toast(clip(out.stderr || 'No file dialog here; type @path in the message instead.', 120))
    return
  }
  const picked = JSON.parse(out.stdout) as string[]
  const all = (await $.state.get(ATTACHMENTS)).value ?? {}
  const list = all[id] ?? []
  await $.state.set(ATTACHMENTS, { ...all, [id]: [...list, ...picked.filter(path => !list.includes(path))] })
}

async function detach($: EngineInterface, id: string, path: string) {
  const all = (await $.state.get(ATTACHMENTS)).value ?? {}
  await $.state.set(ATTACHMENTS, { ...all, [id]: (all[id] ?? []).filter(one => one !== path) })
}

async function run($: EngineInterface, args: string[]) {
  const stream = $.process.spawn({
    argv: ['python3', `${$.plugin.root}/scripts/delegate.py`, '--no-color', ...args],
    cwd: await $.session.root(),
  })
  for await (const _chunk of stream) {
    // drained: the pane reads the transcript file, not this output
  }
  return stream.result
}

// The person's message: sent now, or queued behind the running turn. The lead agent hears of it
// once the reply is in (reportUserTurns).
async function send($: EngineInterface, id: string, typed: string) {
  const text = typed.trim()
  const files = ((await $.state.get(ATTACHMENTS)).value ?? {})[id] ?? []
  if (!text && !files.length) return
  await setDraft($, id, '')
  await $.state.set(ATTACHMENTS, { ...((await $.state.get(ATTACHMENTS)).value ?? {}), [id]: [] })
  await $.state.set(SENDING, id)
  try {
    const flags = files.flatMap(path => ['--attach', path])
    await run($, ['send', id, '--as-user', '--detach', ...flags, '--', text || 'See the attached files.'])
  } finally {
    await $.state.set(SENDING, '')
  }
  toEnd($, id)
  await poll($)
}

// The list, and the chat opened last beside it.
async function openPanes($: EngineInterface, isAsked: boolean) {
  await poll($)
  await $.ui.open({ id: LIST, title: LIST_TITLE, columns: 36, ...(isAsked ? { focus: true as const } : {}) })
  const id = (await $.state.get(SELECTED)).value ?? ''
  const list = (await $.state.get(DELEGATIONS)).value ?? []
  const chat = list.find(one => one.id === id) ?? list.filter(one => !one.archived).at(-1)
  if (chat) await openChat($, chat.id, false)
}

// Chats by project tag: named projects alphabetically, then the untagged.
function byProject(list: Delegation[]) {
  const groups = new Map<string, Delegation[]>()
  for (const one of list) groups.set(one.project, [...(groups.get(one.project) ?? []), one])
  return [...groups.entries()].sort(([a], [b]) => (a === '' ? 1 : b === '' ? -1 : a.localeCompare(b)))
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    // State outlives a reload, files are the truth: drop what was read from them so the first poll
    // reads it again in this version's shape.
    await $.state.set(DELEGATIONS, [])
    await $.state.set(QUEUE, {})
    await $.state.set(EXTRA, {})
    await $.state.set(MODELS, {})
    brands = JSON.parse(await $.fs.read(`${$.plugin.root}/assets/brands.json`))
    await $.command.register({ name: 'delegations', description: 'Show delegations to other agents in a pane' })
    // A convenience, so a refusal (a host without plugin tools) doesn't stop the pane from starting.
    await $.tool
      .register({
        name: 'pane',
        description: 'Open the Delegations panes, which show delegations to other coding agents. Use when the user asks to see them.',
        isDeferred: true,
      })
      .catch(() => undefined)
    $.clock.every(700, () => void poll($))
    $.clock.every(SPIN_MS, () => void spin($).catch(() => undefined))
    return next(e)
  })

  on('command.run', { command: 'delegations' }, async $ => {
    await openPanes($, true)
    return { text: 'Delegations opened.' }
  })

  on('tool.call', { tool: 'mcp__delegate__pane' }, async $ => {
    await openPanes($, false)
    return { result: 'Delegations opened.' }
  })

  on('ui.message', { component: 'Pane', requestId: LIST }, async ($, e) => {
    await onNav($, e.data as NavAction)
    return {}
  })

  // Delegations is pinned: answering without next keeps it open when the person closes it.
  on('ui.close', async ($, e, next) => {
    if (e.id === LIST && e.origin.kind === 'person') return { value: undefined }
    const id = chatOf(e.id)
    if (id) {
      eventsOf.delete(id)
      following.delete(id)
      edges.delete(id)
      titles.delete(e.id)
    }
    return next(e)
  })

  // A chat scrolls natively. Reaching its end makes new output follow; reaching either edge of what
  // is drawn draws the next batch past it.
  on('ui.scroll', { component: 'Pane' }, async ($, e, next) => {
    const id = chatOf(e.requestId)
    if (id && Number.isFinite(e.offset)) {
      const edge = edges.get(id) ?? { hasEarlier: false, hasLater: false }
      const atBottom = e.offset >= e.contentRows - e.bodyRows - 1
      following.set(id, atBottom && !edge.hasLater)
      const extra = ((await $.state.get(EXTRA)).value ?? {})[id] ?? 0
      if (e.offset <= 2 && edge.hasEarlier && e.origin.kind === 'person') await setExtra($, id, extra + EARLIER)
      else if (atBottom && edge.hasLater && e.origin.kind === 'person') await setExtra($, id, Math.max(0, extra - EARLIER))
    }
    return next(e)
  })

  // Delegations: the chat list, grouped by project.
  on('ui.render', { component: 'Pane', requestId: LIST }, async ($, e) => {
    const ui = $.ui.resolve(e)
    const { Box, Button } = ui
    // Terminal and desktop draw the list as a Client, which tells a right click from a left one;
    // VS Code and mobile get a button per chat.
    const Client = (e.surface === 'terminal' || e.surface === 'desktop') && 'Client' in ui ? ui.Client : undefined
    const list = await read($, delegations)
    const id = await read($, selected)
    const active = list.filter(one => !one.archived)
    const archived = list.filter(one => one.archived)
    const groups = byProject(active)
    const navProps: NavProps = {
      hoverColor: e.surface === 'desktop' ? '#80808033' : '#3A3A3A',
      selected: id,
      archived: archived.length,
      groups: groups.map(([project, chats]) => ({
        project,
        chats: chats.map(d => ({
          id: d.id,
          name: clip(d.name ?? d.title ?? d.id, 48),
          glyph: brandOf(d.harness).glyph,
          color: brandOf(d.harness).color,
          running: d.status === 'running',
          unread: isUnread(d),
        })),
      })),
    }
    // nav.tsx draws a project line, a blank and a line per chat, a blank after each project, the
    // archive's line, and room for its menu under the last.
    const lines = groups.reduce((sum, [, chats]) => sum + 2 + chats.length * 2, 0) + 1 + 5
    if (Client) {
      return <Client key="nav" module="./nav.tsx" props={navProps} width={e.props.bodyColumns} height={Math.max(e.props.scroll.bodyRows, lines)} />
    }
    return (
      <Box key="nav" flexDirection="column" gap={1}>
        {active.map(d => (
          <Button
            key={`tab-${d.id}`}
            label={`${d.status === 'running' ? '… ' : ''}${brandOf(d.harness).glyph} ${clip(d.name ?? d.id, 32)}${isUnread(d) ? ' ●' : ''}`}
            variant={d.id === id ? 'primary' : 'secondary'}
            onPress={() => void openChat($, d.id, true)}
          />
        ))}
        <Button key="archived" label={`Archived (${archived.length})`} plain onPress={() => void openArchive($)} />
      </Box>
    )
  })

  // A chat (one tab per chat), or the archive: one document the surface scrolls, a chat's header
  // first and its composer last.
  on('ui.render', { component: 'Pane' }, async ($, e, next) => {
    const id = chatOf(e.requestId)
    if (!id && e.requestId !== ARCHIVE) return next(e)
    const ui = $.ui.resolve(e)
    const { Box, Text, Button, Markdown } = ui
    const Svg = 'Svg' in ui ? ui.Svg : undefined
    const Input = 'Input' in ui ? ui.Input : undefined
    const Select = 'Select' in ui ? ui.Select : undefined
    const list = await read($, delegations)
    const where = await read($, page)
    const busy = await read($, sending)
    const modelLists = await read($, models)
    const namingId = await read($, naming)
    const draftOf = await read($, drafts)
    const filesOf = await read($, attachments)
    const queues = await read($, queue)
    const extras = await read($, earlier)
    const foldOf = await read($, folds)
    const current = list.find(one => one.id === id)
    const archived = list.filter(one => one.archived)
    const projects = [...new Set(list.map(one => one.project).filter(Boolean))].sort()

    const logo = (who: string, size = 16) => {
      const brand = brandOf(who)
      return Svg && brand.svg ? (
        <Svg source={brand.svg} alt={brand.name} width={size} height={size} />
      ) : (
        <Text color={brand.color} bold>
          {brand.glyph}
        </Text>
      )
    }
    // ---- the archive

    if (e.requestId === ARCHIVE) {
      return (
        <Box key="archive-view" flexDirection="column" gap={1} paddingX={1}>
          <Text bold>Archived chats</Text>
          {archived.length === 0 ? <Text dimColor>Nothing archived. Right-click a chat to archive it; its transcript stays.</Text> : null}
          {archived.map(d => (
            <Box key={`archived-${d.id}`} flexDirection="row" gap={1} alignItems="center">
              {logo(d.harness)}
              <Text>{d.name}</Text>
              <Text dimColor>{d.project ? `${d.project} · ${d.id}` : d.id}</Text>
              <Button key={`open-${d.id}`} label="Open" plain onPress={() => void openChat($, d.id, true)} />
              <Button key={`restore-${d.id}`} label="Unarchive" plain onPress={() => void setMeta($, d.id, ['--unarchive'])} />
            </Box>
          ))}
        </Box>
      )
    }
    if (!current) return <Text dimColor>This chat was deleted.</Text>

    // ---- the header

    const brand = brandOf(current.harness)
    const fold = foldOf[current.id]
    // Model, effort and speed, each its own picker. A Select takes at most 64 options.
    const choices = modelLists[current.harness] ?? []
    const modelValue = current.model || DEFAULT
    const model = choices.find(one => one.id === modelValue) ?? { id: modelValue, label: modelValue, efforts: [], speeds: [] }
    const modelOptions = [model, ...choices.filter(one => one.id !== modelValue)].slice(0, SELECT_MAX)
    const efforts = model.efforts?.length ? model.efforts : (choices[0]?.efforts ?? [])
    const effortValue = current.effort || DEFAULT
    const speeds = model.speeds ?? []
    const projectOptions = [
      { value: NO_PROJECT, label: 'No project' },
      ...projects.slice(0, SELECT_MAX - 2).map(name => ({ value: name, label: name })),
      { value: NEW_PROJECT, label: 'New project…' },
    ]
    const onProject = (value: string) => {
      if (value === NEW_PROJECT) void $.state.set(NAMING, current.id)
      else void setMeta($, current.id, value === NO_PROJECT ? ['--no-project'] : ['--project', value])
    }
    const isRunning = current.status === 'running' || busy === current.id
    const files = filesOf[current.id] ?? []

    // The gap is a whole row, not a named size: the desktop drops a tree whose gap is "sm" without a word.
    const header = (
      <Box key="chat-header" flexDirection="column" gap={1} flexShrink={0}>
        <Box flexDirection="row" gap={1} alignItems="center">
          {logo(current.harness)}
          <Text bold>{current.name}</Text>
          <Text dimColor>
            {brand.name} · {current.mode === 'write' ? 'writes in its worktree' : 'read-only'} · {current.turns} turns
          </Text>
          {current.archived ? (
            <Button key="unarchive" label="Unarchive" plain onPress={() => void setMeta($, current.id, ['--unarchive'])} />
          ) : null}
        </Box>
        <Box flexDirection="row" flexWrap="wrap" gap={2} alignItems="center">
          {Select ? (
            <Select key={`project-${current.id}`} label="Project" value={current.project || NO_PROJECT} options={projectOptions} onSelect={onProject} />
          ) : (
            <Text dimColor>Project: {current.project || 'none'}</Text>
          )}
          {Select && choices.length > 0 ? (
            <Select
              key={`model-${current.id}`}
              label="Model"
              value={modelValue}
              options={modelOptions.map(one => ({ value: one.id, label: one.label }))}
              onSelect={value => void choose($, current.id, '--model', value)}
            />
          ) : (
            <Text dimColor>Model: {modelValue}</Text>
          )}
          {Select && efforts.length > 0 ? (
            <Select
              key={`effort-${current.id}`}
              label="Effort"
              value={efforts.includes(effortValue) ? effortValue : DEFAULT}
              options={[{ value: DEFAULT, label: 'Default' }, ...efforts.map(level => ({ value: level, label: level }))]}
              onSelect={value => void choose($, current.id, '--effort', value)}
            />
          ) : null}
          {Select && speeds.length > 0 ? (
            <Select
              key={`speed-${current.id}`}
              label="Speed"
              value={current.speed || DEFAULT}
              options={[{ value: DEFAULT, label: 'Standard' }, ...speeds.map(speed => ({ value: speed, label: speed }))]}
              onSelect={value => void choose($, current.id, '--speed', value)}
            />
          ) : null}
          <Button
            key={`thinking-${current.id}`}
            label={fold?.hideThinking ? '◌ Show thinking' : '◍ Hide thinking'}
            plain
            dimColor
            onPress={() => void setFold($, current.id, one => ({ ...one, hideThinking: !one.hideThinking, toggled: [] }))}
          />
          <Button
            key={`tools-${current.id}`}
            label={fold?.hideTools ? '▤ Unfold short output' : '▤ Fold all output'}
            plain
            dimColor
            onPress={() => void setFold($, current.id, one => ({ ...one, hideTools: !one.hideTools, toggled: [] }))}
          />
        </Box>
        {namingId === current.id && Input ? (
          <Box flexDirection="row" gap={1} alignItems="center">
            <Box flexDirection="column" flexGrow={1}>
              <Input
                key={`project-name-${current.id}`}
                label="New project"
                placeholder="name, then Enter"
                autoFocus
                onSubmit={value => {
                  void $.state.set(NAMING, '')
                  if (value.trim()) void setMeta($, current.id, ['--project', value.trim()])
                }}
              />
            </Box>
            <Button key={`project-name-close-${current.id}`} label="✕" plain dimColor onPress={() => void $.state.set(NAMING, '')} />
          </Box>
        ) : null}
      </Box>
    )

    // ---- the conversation: every event, the newest at the bottom, scrolled by the surface

    void where // the events' revision: a change redraws
    // Paths read relative to the project (or the delegate's worktree), as the person would write them.
    const root = await $.session.root()
    const prefixes = [`file://${root}/.delegate/${current.id}/worktree/`, `${root}/.delegate/${current.id}/worktree/`, `file://${root}/`, `${root}/`]
    const relative = (text: string) => prefixes.reduce((out, prefix) => out.split(prefix).join(''), text)
    const events = (eventsOf.get(current.id) ?? []).map(ev => ({ ...ev, text: relative(ev.text) }))
    const all = toRows(events, current.harness, Math.max(30, e.props.bodyColumns - 6), fold)
    const extra = extras[current.id] ?? 0
    // A row costs its text and a few characters of its own; a head row its logo's source and buttons too.
    const cost = (row: Row) => row.text.length + 4 + (row.kind === 'head' ? (brandOf(row.ev.from).svg?.length ?? 0) + 16 : 0)
    let first = all.length
    let used = 0
    for (; first > 0 && used < DRAWN_CHARS + extra; first--) used += cost(all[first - 1]!)
    let last = all.length
    for (; last > first + 1 && used > DRAWN_CHARS; last--) used -= cost(all[last - 1]!)
    edges.set(current.id, { hasEarlier: first > 0, hasLater: last < all.length })
    const line = (row: Row) => {
      const ev = row.ev
      if (row.kind === 'gap') return <Box key={row.key} flexShrink={0}><Text> </Text></Box>
      if (row.kind === 'head') {
        const who = brandOf(ev.from)
        const isTalk = ev.kind === 'message' || ev.kind === 'final'
        const block = row.key.slice(0, -2) // the event's key, without "-h"
        return (
          <Box key={row.key} flexDirection="row" gap={1} alignItems="center" flexShrink={0}>
            {row.foldable ? (
              <Button
                key={`fold-${row.key}`}
                label={row.folded ? '▸' : '▾'}
                plain
                dimColor
                onPress={() => void setFold($, current.id, one => toggleBlock(one, block))}
              />
            ) : null}
            {logo(ev.from, 14)}
            <Text color={isTalk ? who.color : undefined} bold={isTalk} dimColor={!isTalk} italic={ev.kind === 'thinking'} wrap="truncate-end">
              {row.text}
            </Text>
            {isTalk ? (
              <Button key={`copy-${row.key}`} label="⧉ Copy" plain dimColor onPress={press => void $.ui.copy({ text: ev.text, surface: press.surface })} />
            ) : null}
          </Box>
        )
      }
      if (row.kind === 'md') {
        return (
          <Box key={row.key} paddingLeft={3} flexShrink={0} flexDirection="column">
            <Markdown key={`md-${row.key}`} text={row.text} />
          </Box>
        )
      }
      const isTalk = ev.kind === 'message' || ev.kind === 'final'
      return (
        <Box key={row.key} paddingLeft={3} flexShrink={0}>
          <Text dimColor={!isTalk} italic={ev.kind === 'thinking'} color={ev.kind === 'error' ? 'red' : undefined} wrap="truncate-end">
            {row.text || ' '}
          </Text>
        </Box>
      )
    }

    // ---- the composer ends the document: at the newest line it is on the pane's bottom edge. While
    // the delegate works, what is sent waits in its queue. The header's pickers are a click away.

    const pending = queues[current.id] ?? []
    const composer =
      current.status === 'closed' ? (
        <Text dimColor>Closed.</Text>
      ) : (
        <Box key="composer" flexDirection="column" gap={1} flexShrink={0}>
          {pending.map((item, i) => (
            <Box key={`queued-${i}`}>
              <Text dimColor>
                ⏳ queued{item.from === 'user' ? '' : ` (${item.from})`}: {clip(item.text, 100)}
                {item.attachments.length ? ` · 📎 ${item.attachments.length}` : ''}
              </Text>
            </Box>
          ))}
          {isRunning ? (
            <Box flexDirection="row" gap={1} alignItems="center">
              <Text color={brand.color}>{current.harness} is working on turn {current.turns}…</Text>
              <Button key="stop" label="Stop" plain dimColor onPress={() => void run($, ['stop', current.id])} />
            </Box>
          ) : null}
          <Box flexDirection="row" flexWrap="wrap" gap={1} alignItems="center">
            {files.map(path => (
              <Box key={`file-${path}`} flexDirection="row" alignItems="center">
                <Text>📎 {baseName(path)}</Text>
                <Button key={`unfile-${path}`} label="×" plain dimColor onPress={() => void detach($, current.id, path)} />
              </Box>
            ))}
            <Button key={`pick-files-${current.id}`} label="📎 Attach files" plain dimColor onPress={() => void pickFiles($, current.id, false)} />
            <Button key={`pick-folder-${current.id}`} label="📁 Attach folder" plain dimColor onPress={() => void pickFiles($, current.id, true)} />
            <Button
              key={`to-header-${current.id}`}
              label="⚙ Model and project"
              plain
              dimColor
              onPress={() => void $.ui.scroll({ to: 'start', in: CHAT + current.id }).catch(() => undefined)}
            />
          </Box>
          {Input ? (
            <Box flexDirection="row" gap={1} alignItems="center">
              {logo(current.harness)}
              <Box flexDirection="column" flexGrow={1}>
                <Input
                  key={`message-${current.id}`}
                  rows={2}
                  value={draftOf[current.id] ?? ''}
                  placeholder={
                    isRunning
                      ? `Queue a message for ${current.harness}; it runs when this turn ends.`
                      : `Message ${current.harness} yourself. @path attaches a file too.`
                  }
                  submitLabel={isRunning ? 'Queue' : 'Send'}
                  onInput={value => void setDraft($, current.id, value)}
                  onSubmit={value => void send($, current.id, value)}
                />
              </Box>
            </Box>
          ) : null}
        </Box>
      )

    return (
      <Box flexDirection="column" paddingX={1}>
        <Box key="header-panel" flexDirection="column" borderStyle="round" borderColor="promptBorder" paddingX={1} marginBottom={1}>
          {header}
        </Box>
        <Box key="conversation" flexDirection="column">
          {all.slice(first, last).map(line)}
        </Box>
        <Box key="composer-panel" flexDirection="column" marginTop={1} borderStyle="round" borderColor="promptBorder" paddingX={1}>
          {composer}
        </Box>
      </Box>
    )
  })
}
