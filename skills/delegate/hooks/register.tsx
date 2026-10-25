import { atom, read } from 'claude-code'
import type { EngineInterface, Register } from 'claude-code'

import type {
  Brand,
  DelegateEvent,
  Delegation,
  ModelOption,
  NavAction,
  NavProps,
  QueuedMessage,
} from '../types'

// The pane reads what scripts/delegate.py writes under <project>/.delegate/ and draws it, one screen
// tall: the chat sidebar (hooks/nav.tsx) on the left; on the right the chat's header at the top, its
// conversation in the middle, and the composer at the bottom. The conversation scrolls natively;
// the sidebar, header and composer float over it, placed at the window's edges on every scroll.

const PANE = 'delegate'
const TITLE = 'Delegate'
const ARCHIVE = '__archived' // the view of archived chats, selected like a chat
const NO_PROJECT = '__none'
const NEW_PROJECT = '__new'
const DEFAULT = 'default'
const SELECT_MAX = 64
// A drawing has a size limit, so the conversation draws its newest rows up to DRAWN_CHARS characters
// of text; scrolling to the top of them draws the next older batch (EARLIER more each time). The engine
// draws 100,000 characters of a tree, so past DRAWN_MAX the newest rows give way, and scrolling to the
// bottom brings them back.
const DRAWN_CHARS = 40_000
const DRAWN_MAX = 80_000
// While the person scrolls, the floating panels fade out, and fade back in once the wheel has been
// still for SETTLE_MS. There is no opacity to animate, so a fade is FADE_STEPS frames of alpha colours:
// a cover in the panel's colour rises over its contents, then the panel's background thins away.
const SETTLE_MS = 450
const STEP_MS = 35
const FADE_STEPS = 8
const EARLIER = 20_000
// The floating panels' colour, from the person's theme (read at session start).
let panelHex = '#101010'
const withAlpha = (hex: string, alpha: number) =>
  alpha >= 1 ? hex : `${hex}${Math.round(Math.max(0, Math.min(1, alpha)) * 255).toString(16).padStart(2, '0').toUpperCase()}`

// Helpers write state through $.state with these refs; the render hook reads the atoms over them.
const DELEGATIONS = { plugin: 'delegate', key: 'delegations' } as const
const SELECTED = { plugin: 'delegate', key: 'selected' } as const
const PAGE = { plugin: 'delegate', key: 'page' } as const
const SCROLL = { plugin: 'delegate', key: 'scroll' } as const
const SENDING = { plugin: 'delegate', key: 'sending' } as const
const MODELS = { plugin: 'delegate', key: 'models' } as const
const NAMING = { plugin: 'delegate', key: 'naming' } as const
const DRAFTS = { plugin: 'delegate', key: 'drafts' } as const
const ATTACHMENTS = { plugin: 'delegate', key: 'attachments' } as const
const QUEUE = { plugin: 'delegate', key: 'queue' } as const
const SIDEBAR = { plugin: 'delegate', key: 'sidebar' } as const
const EXTRA = { plugin: 'delegate', key: 'extra' } as const
const LAYERS = { plugin: 'delegate', key: 'layers' } as const
const delegations = atom(DELEGATIONS, [])
const selected = atom(SELECTED, '')
// A revision of the selected chat's events (they live in allEvents): a change redraws.
const page = atom(PAGE, { start: 0, end: 0, total: 0 })
// The window's first row, as the last scroll left it: the floating layers sit at it.
const scroll = atom(SCROLL, 0)
const sending = atom(SENDING, '')
const models = atom(MODELS, {})
// The chat whose project is being named in a new-project field, '' for none.
const naming = atom(NAMING, '')
// Per chat: the unsent message and the paths attached to it.
const drafts = atom(DRAFTS, {})
const attachments = atom(ATTACHMENTS, {})
// Messages queued behind the selected chat's running turn.
const queue = atom(QUEUE, [])
// The sidebar's width in columns, dragged by its edge and kept across sessions.
const sidebar = atom(SIDEBAR, 30)
// Characters of older conversation drawn beyond DRAWN_CHARS, grown by scrolling to the top.
const earlier = atom(EXTRA, 0)
// How far the floating panels have faded: 0 shown, FADE_STEPS gone.
const layers = atom(LAYERS, 0)

// Names, colours, glyphs and SVG logos, from assets/brands.json (shared with the script and the MCP App).
let brands: Record<string, Brand> = {}
const brandOf = (who: string): Brand =>
  brands[who] ?? brands.lead ?? { name: who, color: '#8A8A8A', glyph: '◆', svg: '' }

// File path -> mtime at the last read. Module state, so a reload re-reads everything once.
const stamps = new Map<string, number>()
let isPolling = false
const fetchingModels = new Set<string>()
const markingSeen = new Set<string>()
// Per chat, the last finished turn the lead agent has been told about (for the person's own messages).
const reported = new Map<string, number>()
// Every event of the selected chat, read from its events.jsonl.
let allEvents: DelegateEvent[] = []
// Whether the window is at the newest line, so new output keeps it there.
let isFollowing = true
// Whether older, or newer, rows exist than the ones drawn.
let hasEarlier = false
let hasLater = false
// When the person last moved the wheel, and where the fade is heading.
let lastWheel = 0
let fadeTarget = 0
let isFading = false
// The pane's size at the last draw, so a resize is noticed.
let lastSize = ''

const clip = (text: string, n: number) => {
  const flat = text.replace(/\s+/g, ' ').trim()
  return flat.length <= n ? flat : `${flat.slice(0, n - 1)}…`
}

const baseName = (path: string) => path.replace(/\/+$/, '').split('/').pop() ?? path

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

// Every event of the selected chat as rows at a width: a header row per event, then its whole body.
// Messages and replies are markdown, one row per block (a paragraph, a list, a fenced code block),
// drawn as Markdown; the rest is plain lines. `height` is the rows a row is expected to take.
type Row = { key: string; ev: DelegateEvent; kind: 'head' | 'body' | 'md' | 'gap'; text: string; height: number }

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

function toRows(list: DelegateEvent[], harness: string, width: number): Row[] {
  const rows: Row[] = []
  list.forEach((ev, n) => {
    const key = `${ev.turn}:${ev.ts}`
    const label = {
      message: ev.from === harness ? ev.from : `${ev.from} → ${harness}`,
      final: `${ev.from} · turn ${ev.turn} · ${ev.seconds ?? 0}s · STATUS: ${ev.status ?? '?'}`,
      thinking: 'thinking',
      tool: `› ${ev.text.split('\n')[0]}`,
      tool_result: '↳ output',
      error: '✗ error',
      status: `· ${ev.text}`,
    }[ev.kind]
    rows.push({ key: `${key}-h`, ev, kind: 'head', text: label, height: 1 })
    if (ev.kind === 'message' || ev.kind === 'final') {
      const files = ev.kind === 'message' && ev.attachments?.length ? `\n\n📎 ${ev.attachments.join(', ')}` : ''
      markdownBlocks(ev.text + files).forEach((text, i) => {
        rows.push({ key: `${key}-${i}`, ev, kind: 'md', text, height: wrap(text, width).length + 1 })
      })
    } else {
      const body = ev.kind === 'tool' ? ev.text.split('\n').slice(1).join('\n') : ev.kind === 'status' ? '' : ev.text
      if (body.trim()) {
        wrap(body, width).forEach((text, i) => rows.push({ key: `${key}-${i}`, ev, kind: 'body', text, height: 1 }))
      }
    }
    if (n < list.length - 1) rows.push({ key: `${key}-gap`, ev, kind: 'gap', text: ' ', height: 1 })
  })
  return rows
}

// Tells the render hook the events changed; they live in allEvents, not in state.
async function showPage($: EngineInterface) {
  await $.state.set(PAGE, { start: 0, end: allEvents.length, total: allEvents.length })
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

async function poll($: EngineInterface) {
  if (isPolling) return
  isPolling = true
  try {
    const base = `${await $.session.root()}/.delegate`
    if (!(await $.fs.exists(base))) return
    const before = (await $.state.get(DELEGATIONS)).value ?? []
    const dirs = (await $.fs.list(base)).filter(entry => entry.kind === 'dir')
    let isDirty = dirs.length !== before.length
    const now: Delegation[] = []
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
      if (fresh.status === 'running' && old?.status !== 'running') {
        await $.state.set(SELECTED, fresh.id)
        void $.ui.open({ id: PANE, title: TITLE }).then(() => toEnd($))
      }
      if (old?.status === 'running' && fresh.status !== 'running') {
        $.ui.toast(`${brandOf(fresh.harness).glyph} ${fresh.name} replied (STATUS: ${fresh.agentStatus || '?'})`)
      }
    }
    if (isDirty) await $.state.set(DELEGATIONS, now.sort((a, b) => a.created - b.created))

    const running = now.filter(one => one.status === 'running')
    $.ui.status(running.length ? running.map(one => `${brandOf(one.harness).glyph} ${one.name} working`).join('  ') : undefined)

    let id = (await $.state.get(SELECTED)).value ?? ''
    if (id !== ARCHIVE && !now.some(one => one.id === id)) {
      id = now.filter(one => !one.archived).at(-1)?.id ?? ''
      await $.state.set(SELECTED, id)
    }
    const current = now.find(one => one.id === id)
    if (!current) return
    void loadModels($, current.harness)
    if (isUnread(current) && (await $.ui.panes()).some(pane => pane.id === PANE && pane.isPlaced)) {
      void markSeen($, current.id)
    }
    const log = `${base}/${id}/events.jsonl`
    if (await changed($, log)) {
      allEvents = parseLines<DelegateEvent>(await $.fs.read(log))
      await showPage($)
      if (isFollowing) $.clock.after(50, () => toEnd($))
    }
    const queued = `${base}/${id}/queue.jsonl`
    if (await changed($, queued)) {
      await $.state.set(QUEUE, parseLines<QueuedMessage>(await $.fs.read(queued)))
    }
  } finally {
    isPolling = false
  }
}

// Fades the floating panels out on the first wheel move, and back in once the wheel is still.
function fadeOut($: EngineInterface) {
  lastWheel = Date.now()
  fadeTo($, FADE_STEPS)
  $.clock.after(SETTLE_MS, () => {
    if (Date.now() - lastWheel >= SETTLE_MS - 20) fadeTo($, 0)
  })
}

// Steps the fade one frame at a time toward `target`; a new target turns it around mid-way.
function fadeTo($: EngineInterface, target: number) {
  fadeTarget = target
  if (isFading) return
  isFading = true
  const step = async () => {
    const held = (await $.state.get(LAYERS)).value
    const now = typeof held === 'number' && Number.isFinite(held) ? held : 0
    if (now === fadeTarget) {
      isFading = false
      return
    }
    await $.state.set(LAYERS, now + Math.sign(fadeTarget - now))
    $.clock.after(STEP_MS, () => void step())
  }
  void step()
}

// Shows the newest line: the window goes to the end, and keeps following new output from there.
function toEnd($: EngineInterface) {
  isFollowing = true
  if (hasLater) void $.state.set(EXTRA, 0)
  const place = async () => {
    await $.ui.scroll({ to: 'end', in: PANE })
  }
  void place().catch(() => undefined)
  $.clock.after(300, () => void place().catch(() => undefined))
}

async function select($: EngineInterface, id: string) {
  const base = `${await $.session.root()}/.delegate`
  stamps.delete(`${base}/${id}/events.jsonl`)
  stamps.delete(`${base}/${id}/queue.jsonl`)
  allEvents = []
  await $.state.set(SELECTED, id)
  await $.state.set(QUEUE, [])
  await $.state.set(SCROLL, 0)
  await $.state.set(EXTRA, 0)
  await showPage($)
  await poll($)
  toEnd($)
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

// What the sidebar posts: a click, a menu choice, a rename, a new width.
async function onNav($: EngineInterface, action: NavAction) {
  switch (action.type) {
    case 'select':
      return select($, action.target)
    case 'resize':
      // The list draws inside the panel's border and padding: four columns narrower than the panel.
      await $.state.set(SIDEBAR, action.width + 4)
      return $.store.set('sidebar', action.width + 4)
    case 'archive':
      return setMeta($, action.target, ['--archive'])
    case 'rename':
      return setMeta($, action.target, ['--name', action.value])
    case 'rename-project':
      await run($, ['rename-project', action.target, action.value])
      return poll($)
    case 'delete':
      await run($, ['delete', action.target])
      return poll($)
  }
}


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
  await $.state.set(SCROLL, 0)
  try {
    const flags = files.flatMap(path => ['--attach', path])
    await run($, ['send', id, '--as-user', '--detach', ...flags, '--', text || 'See the attached files.'])
  } finally {
    await $.state.set(SENDING, '')
  }
  await poll($)
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
    await $.state.set(QUEUE, [])
    await $.state.set(MODELS, {})
    await $.state.set(SCROLL, 0)
    await $.state.set(LAYERS, 0)
    const width = await $.store.get('sidebar')
    if (typeof width === 'number') await $.state.set(SIDEBAR, width)
    brands = JSON.parse(await $.fs.read(`${$.plugin.root}/assets/brands.json`))
    await $.command.register({ name: 'delegations', description: 'Show delegations to other agents in a pane' })
    // A convenience, so a refusal (a host without plugin tools) doesn't stop the pane from starting.
    await $.tool
      .register({
        name: 'pane',
        description: 'Open the Delegate pane, which shows delegations to other coding agents. Use when the user asks to see it.',
        isDeferred: true,
      })
      .catch(() => undefined)
    $.clock.every(700, () => void poll($))
    // The panels' colour follows the theme; looked up without holding the start.
    void $.config
      .list()
      .then(rows => {
        const theme = String(rows.find(row => row.key === 'theme')?.value ?? '')
        panelHex = theme.includes('light') ? '#F3F3F1' : '#101010'
      })
      .catch(() => undefined)
    return next(e)
  })

  on('command.run', { command: 'delegations' }, async $ => {
    await poll($)
    await $.ui.open({ id: PANE, title: TITLE, focus: true })
    toEnd($)
    return { text: 'Delegate pane opened.' }
  })

  on('tool.call', { tool: 'mcp__delegate__pane' }, async $ => {
    await poll($)
    await $.ui.open({ id: PANE, title: TITLE })
    toEnd($)
    return { result: 'Delegate pane opened.' }
  })

  on('ui.message', { component: 'Pane', requestId: PANE }, async ($, e) => {
    await onNav($, e.data as NavAction)
    return {}
  })

  // The window scrolls natively; its new first row redraws the floating layers there, and whether it
  // reached the end decides if new output follows. The person's scrolling fades the layers out.
  on('ui.scroll', { component: 'Pane', requestId: PANE }, async ($, e, next) => {
    if (e.origin.kind === 'person') fadeOut($)
    if (Number.isFinite(e.offset)) {
      const atBottom = e.offset >= e.contentRows - e.bodyRows - 1
      isFollowing = atBottom && !hasLater
      await $.state.set(SCROLL, e.offset)
      const extra = (await $.state.get(EXTRA)).value ?? 0
      if (e.offset <= 2 && hasEarlier && e.origin.kind === 'person') await $.state.set(EXTRA, extra + EARLIER)
      else if (atBottom && hasLater && e.origin.kind === 'person') await $.state.set(EXTRA, Math.max(0, extra - EARLIER))
    }
    return next(e)
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const ui = $.ui.resolve(e)
    const { Box, Text, Button, Markdown } = ui
    const Svg = 'Svg' in ui ? ui.Svg : undefined
    const Input = 'Input' in ui ? ui.Input : undefined
    const Select = 'Select' in ui ? ui.Select : undefined
    // Terminal and desktop draw Clients (the sidebar and the scrolling conversation); VS Code and
    // mobile get buttons and a plain list that the surface scrolls.
    const Client = (e.surface === 'terminal' || e.surface === 'desktop') && 'Client' in ui ? ui.Client : undefined
    const list = await read($, delegations)
    const id = await read($, selected)
    const where = await read($, page)
    const offset = await read($, scroll)
    const busy = await read($, sending)
    const modelLists = await read($, models)
    const namingId = await read($, naming)
    const draftOf = await read($, drafts)
    const filesOf = await read($, attachments)
    const pending = await read($, queue)
    const navWidth = await read($, sidebar)
    const extra = await read($, earlier)
    // A value an older version stored (a word, not a step) reads as fully shown.
    const stored = await read($, layers)
    const fade = typeof stored === 'number' && Number.isFinite(stored) ? stored : 0
    const current = list.find(one => one.id === id)
    const active = list.filter(one => !one.archived)
    const archived = list.filter(one => one.archived)
    const groups = byProject(active)
    const projects = [...new Set(list.map(one => one.project).filter(Boolean))].sort()
    const bodyRows = e.props.scroll.bodyRows
    const hoverColor = e.surface === 'desktop' ? '#80808033' : '#3A3A3A'

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

    // ---- the sidebar

    const navProps: NavProps = {
      width: navWidth - 4,
      hoverColor,
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
          unread: isUnread(d) && d.id !== id,
        })),
      })),
    }
    const navigation = Client ? (
      <Client key="nav" module="./nav.tsx" props={navProps} width={navWidth - 4} height={bodyRows} />
    ) : (
      <Box key="nav" flexDirection="column" width={navWidth - 4} flexShrink={0} gap={1}>
        {active.map(d => (
          <Button
            key={`tab-${d.id}`}
            label={`${brandOf(d.harness).glyph} ${clip(d.name ?? d.id, 32)}${isUnread(d) && d.id !== id ? ' ●' : ''}`}
            variant={d.id === id ? 'primary' : 'secondary'}
            onPress={() => void select($, d.id)}
          />
        ))}
        <Button key="archived" label={`Archived (${archived.length})`} plain onPress={() => void select($, ARCHIVE)} />
      </Box>
    )

    // ---- the archive view

    const archiveView = (
      <Box key="archive-view" flexDirection="column" gap={1}>
        <Text bold>Archived chats</Text>
        {archived.length === 0 ? <Text dimColor>Nothing archived. Right-click a chat to archive it; its transcript stays.</Text> : null}
        {archived.map(d => (
          <Box key={`archived-${d.id}`} flexDirection="row" gap={1} alignItems="center">
            {logo(d.harness)}
            <Text>{d.name}</Text>
            <Text dimColor>{d.project ? `${d.project} · ${d.id}` : d.id}</Text>
            <Button key={`open-${d.id}`} label="Open" plain onPress={() => void select($, d.id)} />
            <Button key={`restore-${d.id}`} label="Unarchive" plain onPress={() => void setMeta($, d.id, ['--unarchive'])} />
          </Box>
        ))}
      </Box>
    )

    // ---- the chat: header, conversation, composer

    const chatView = () => {
      if (!current) {
        const empty = <Text dimColor>No delegations in this project yet. Ask Claude to hand a task to Codex, Cursor or Antigravity.</Text>
        return { header: null, conversation: empty, composer: null }
      }
      const brand = brandOf(current.harness)

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
            {!isFollowing ? (
              <Box flexGrow={1} justifyContent="flex-end">
                <Button key="latest" label="↓ Jump to the latest" plain onPress={() => toEnd($)} />
              </Box>
            ) : null}
          </Box>
          <Box flexDirection="row" flexWrap="wrap" gap={2} alignItems="center">
            {Select ? (
              <Select
                key={`project-${current.id}`}
                label="Project"
                value={current.project || NO_PROJECT}
                options={projectOptions}
                onSelect={onProject}
              />
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

      // The conversation: every event in full, the newest at the bottom, scrolled by the pane itself.
      void where // the events' revision: a change redraws
      const all = toRows(allEvents, current.harness, Math.max(30, e.props.bodyColumns - navWidth - 8))
      let first = all.length
      let used = 0
      for (; first > 0 && used < DRAWN_CHARS + extra; first--) used += all[first - 1]!.text.length + 40
      let last = all.length
      for (; last > first + 1 && used > DRAWN_MAX; last--) used -= all[last - 1]!.text.length + 40
      const visible = all.slice(first, last)
      hasEarlier = first > 0
      hasLater = last < all.length
      const line = (row: Row) => {
        const ev = row.ev
        if (row.kind === 'gap') return <Box key={row.key} flexShrink={0}><Text> </Text></Box>
        if (row.kind === 'head') {
          const who = brandOf(ev.from)
          const isTalk = ev.kind === 'message' || ev.kind === 'final'
          return (
            <Box key={row.key} flexDirection="row" gap={1} alignItems="center" flexShrink={0}>
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
      const conversation = (
        <Box key="conversation" flexDirection="column">
          {visible.map(line)}
        </Box>
      )

      // The composer, on the pane's bottom edge: while the delegate works, what is sent waits in its queue.
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

      return { header, conversation, composer }
    }

    const view = id === ARCHIVE ? { header: null, conversation: archiveView, composer: null } : chatView()
    // The conversation scrolls natively and the composer ends it, so at the newest line (where the
    // pane opens and follows new output) the composer is on the bottom edge, as the desktop measures
    // it: a plugin can't know how many rows the desktop shows, so nothing is anchored to that edge.
    // The sidebar and header float at the window's top (e.props.scroll.offset), rounded and padded;
    // while scrolled up, the header offers a jump back to the newest line.
    void offset // the window's position as the scroll hook saw it: a change redraws
    // A new pane size fades the panels out and places them again once it settles (as scrolling does).
    const size = `${bodyRows}x${e.props.bodyColumns}`
    if (lastSize && size !== lastSize) $.clock.after(0, () => fadeOut($))
    lastSize = size
    const top = e.props.scroll.offset
    const left = navWidth + 1
    // Fade frames: the first half raises a cover over the panels' contents, the second thins it all away.
    const half = FADE_STEPS / 2
    const cover = fade <= half ? fade / half : (FADE_STEPS - fade) / half
    const ground = fade <= half ? 1 : (FADE_STEPS - fade) / half
    const display = fade >= FADE_STEPS ? 'none' : 'flex'
    const coverBox = cover > 0 ? (
      <Box key="cover" position="absolute" top={0} left={0} right={0} bottom={0} backgroundColor={withAlpha(panelHex, cover)} />
    ) : null
    // Rows the header panel takes: its border, the title line and the pickers (and the new-project
    // field while it is open). The panel sizes to its content; the conversation starts below this.
    const headerRows = view.header ? 2 + 3 + (namingId === id ? 2 : 0) : 0
    const panel = { borderStyle: 'round', borderColor: 'promptBorder', paddingX: 1, backgroundColor: withAlpha(panelHex, ground), display } as const
    return (
      <Box position="relative" flexDirection="column" minHeight={bodyRows}>
        <Box key="flow" flexDirection="column" paddingLeft={left + 2} paddingRight={1} paddingTop={headerRows + 1}>
          <Box key="flow-start" flexDirection="column" marginTop="xs">
            {view.conversation}
          </Box>
          {view.composer ? (
            <Box key="composer-panel" flexDirection="column" marginTop={1} borderStyle="round" borderColor="promptBorder" paddingX={1}>
              {view.composer}
            </Box>
          ) : null}
        </Box>
        {view.header ? (
          <Box key="float-header" position="absolute" top={top} left={left} right={1} flexDirection="column" {...panel}>
            {view.header}
            {coverBox}
          </Box>
        ) : null}
        <Box key="float-sidebar" position="absolute" top={top} left={0} width={navWidth} height={Math.max(10, bodyRows - 1)} flexDirection="column" {...panel}>
          {navigation}
          {coverBox}
        </Box>
      </Box>
    )
  })
}
