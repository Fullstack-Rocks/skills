import { expect, test } from 'claude-code/testing'

// The panes drawn from a fake .delegate/ folder on every surface, so a tree a surface refuses (too
// many Select options, a key twice, a key on a Text) fails here rather than in a session. The test's
// hooks stand in for the engine: the filesystem, the store, the clock, processes and the pane list.

const ROOT = '/proj'
const line = (...rows: object[]) => rows.map(row => JSON.stringify(row)).join('\n') + '\n'

const FILES: Record<string, string> = {
  [`${ROOT}/.delegate/codex-1/state.json`]: JSON.stringify({
    id: 'codex-1', harness: 'codex', status: 'running', agent_status: 'done', mode: 'write',
    turns: 3, title: 'Build the wishlist API', created: 3, model: 'model-3',
  }),
  [`${ROOT}/.delegate/codex-1/meta.json`]: JSON.stringify({ project: 'wishlist', seen_turns: 2 }),
  [`${ROOT}/.delegate/codex-1/events.jsonl`]: line(
    { ts: 1, turn: 1, from: 'claude', kind: 'message', text: 'Build the wishlist API.', attachments: ['/tmp/brief.md'] },
    { ts: 2, turn: 1, from: 'codex', kind: 'thinking', text: 'The routes come first.' },
    // A call and its output in the same millisecond, as Codex logs them.
    { ts: 3, turn: 1, from: 'codex', kind: 'tool', text: `$ ls ${ROOT}/demo/app` },
    { ts: 3, turn: 1, from: 'codex', kind: 'tool_result', text: Array.from({ length: 200 }, (_, i) => `output line ${i} ${'·'.repeat(700)}`).join('\n') },
    { ts: 4, turn: 1, from: 'codex', kind: 'thinking', text: 'Now the handlers.' },
    // Thinking as long as a Cursor review's: 400 lines.
    { ts: 4.5, turn: 1, from: 'codex', kind: 'thinking', text: Array.from({ length: 400 }, (_, i) => `weighing ${i} ${'·'.repeat(110)}`).join('\n') },
    { ts: 5, turn: 1, from: 'codex', kind: 'final', status: 'done', seconds: 9,
      text: Array.from({ length: 20 }, (_, i) => `line ${i}`).join('\n') },
  ),
  [`${ROOT}/.delegate/codex-1/queue.jsonl`]: line({ from: 'user', text: 'Also add a docstring.', attachments: [], ts: 5 }),
  [`${ROOT}/.delegate/cursor-1/state.json`]: JSON.stringify({
    id: 'cursor-1', harness: 'cursor', status: 'idle', agent_status: 'done', mode: 'read',
    turns: 2, title: 'Map the client', created: 2,
  }),
  [`${ROOT}/.delegate/antigravity-1/state.json`]: JSON.stringify({
    id: 'antigravity-1', harness: 'antigravity', status: 'idle', agent_status: 'done', mode: 'read',
    turns: 1, title: 'Map the API', created: 1,
  }),
  [`${ROOT}/.delegate/antigravity-1/meta.json`]: JSON.stringify({ archived: true, project: 'wishlist' }),
}
const DIRS = ['codex-1', 'cursor-1', 'antigravity-1']
// More models than a Select takes, as Cursor lists.
const MODELS = JSON.stringify(
  Array.from({ length: 70 }, (_, i) => ({ id: `model-${i}`, label: `Model ${i}`, efforts: ['low', 'high'], speeds: ['fast'] })),
)

const pane = (requestId: string, title: string) =>
  ({
    plugin: 'delegate',
    component: 'Pane',
    requestId,
    props: {
      title,
      isFocused: false,
      bodyColumns: 100,
      placement: 'dock',
      scroll: { offset: 0, bodyRows: 60 },
      view: {},
    },
  }) as const
const LIST = pane('delegate', '☰ Delegations')
const CHAT = pane('chat-codex-1', 'Build the wishlist API')

const missing = (path: string) => new Error(`ENOENT: ${path}`)

// The characters a drawing spends of the engine's 100,000: texts, labels, alts and logo sources.
const spent = (node: unknown): number => {
  if (typeof node === 'string') return node.length
  if (Array.isArray(node)) return node.reduce((n: number, one) => n + spent(one), 0)
  if (!node || typeof node !== 'object') return 0
  const { props, children } = node as { props?: Record<string, unknown>; children?: unknown }
  const own = ['label', 'text', 'source', 'alt', 'placeholder'].reduce((n, key) => n + spent(props?.[key]), 0)
  return own + spent(children ?? props?.children)
}

{
  test('the panes draw on every surface', { timeoutMs: 20000 }, async ($, on) => {
    on('session.start', (_, e) => ({ cwd: e.cwd }))
    on('session.root', () => ({ value: ROOT }))
    on('clock.every', () => ({ value: undefined }))
    on('clock.after', () => ({ value: undefined }))
    on('command.register', () => ({ value: { command: 'delegations' } }))
    on('tool.register', () => ({ value: { tool: 'mcp__delegate__pane' } }))
    // The panes the plugin opened, each open id once, its latest title kept.
    const open = new Map<string, string>()
    const opened: string[] = []
    on('ui.open', (_, e) => {
      open.set(e.id, e.title ?? e.id)
      opened.push(`${e.id}: ${e.title}`)
      return { value: { isPlaced: true } }
    })
    on('ui.panes', () => ({
      value: [...open].map(([id, title]) => ({ id, title, isShown: true, isFocused: false, isPlaced: true })),
    }))
    on('ui.status', () => ({ value: undefined }))
    on('store.get', () => ({ value: undefined }))
    on('fs.exists', (_, e) => ({ value: e.path === `${ROOT}/.delegate` || e.path in FILES }))
    on('fs.list', () => ({ value: DIRS.map(name => ({ name, kind: 'dir' as const, size: 0, mtimeMs: 1 })) }))
    on('fs.stat', (_, e) => {
      if (!(e.path in FILES)) throw missing(e.path)
      return { value: { kind: 'file' as const, size: FILES[e.path]!.length, mtimeMs: 1, isLink: false } }
    })
    on('fs.read', (_, e) => {
      if (e.path.endsWith('/assets/brands.json')) return { value: '{}' }
      if (!(e.path in FILES)) throw missing(e.path)
      return { value: FILES[e.path]! }
    })
    on('process.run', () => ({
      value: { exitCode: 0, stdout: MODELS, stderr: '', isStdoutTruncated: false, isStderrTruncated: false },
    }))

    await $.session.start({ cwd: ROOT, surface: 'desktop', isInteractive: true })
    await $.command.run({ command: 'delegations' })
    await $.command.run({ command: 'delegations' }) // the model list lands between the two polls
    // The pinned list, and the running chat in a tab of its own: its spinner, its agent's glyph, its name.
    expect(open.get('delegate')).toBe('☰ Delegations')
    expect(open.get('chat-codex-1')).toMatch(/^[⠀-⣿] ◆ Build the wishlist API$/)

    for (const surface of ['terminal', 'desktop', 'vscode', 'mobile'] as const) {
      const ui = await $.ui.mount({ ...CHAT, surface })
      expect(await ui.find({ type: 'Text', text: /queued: Also add a docstring/ })).toBeDefined()
      // The pane scrolls the conversation natively, from its first message: the long output starts
      // folded to a preview of its first lines.
      expect(await ui.find({ type: 'Markdown', text: /Build the wishlist API\./ })).toBeDefined()
      expect(await ui.find({ type: 'Text', text: /↳ output · 200 lines/ })).toBeDefined()
      expect(await ui.find({ type: 'Text', text: /^output line 2$/ })).toBeDefined()
      expect(await ui.find({ type: 'Text', text: /^output line 3$/ })).toBeUndefined()
      // Replies are drawn as markdown.
      expect(await ui.find({ type: 'Markdown', text: /line 19/ })).toBeDefined()
      // Paths read relative to the project.
      expect(await ui.find({ type: 'Text', text: /› \$ ls demo\/app$/ })).toBeDefined()
      // The header's pickers are reachable from the composer.
      expect(await ui.find({ key: 'to-header-codex-1' })).toBeDefined()
      // Model, effort and speed are separate pickers where the surface draws a Select (not mobile).
      if (surface !== 'mobile') {
        expect(await ui.find({ key: 'model-codex-1' })).toBeDefined()
        expect(await ui.find({ key: 'effort-codex-1' })).toBeDefined()
        expect(await ui.find({ key: 'speed-codex-1' })).toBeDefined()
      }
      await ui.unmount()
    }

    // Thinking folds: the chat's switch hides all of it, a block's arrow unfolds that one again.
    const chat = await $.ui.mount({ ...CHAT, surface: 'desktop' })
    expect(await chat.find({ type: 'Text', text: /Now the handlers\./ })).toBeDefined()
    await chat.press({ key: 'thinking-codex-1' })
    expect(await chat.find({ type: 'Text', text: /Now the handlers\./ })).toBeUndefined()
    expect(await chat.find({ type: 'Text', text: /thinking · 1 lines/ })).toBeDefined()
    await chat.press({ key: 'fold-e4-h' })
    expect(await chat.find({ type: 'Text', text: /Now the handlers\./ })).toBeDefined()
    // Long thinking starts folded, as long output does.
    expect(await chat.find({ type: 'Text', text: /thinking · 400 lines/ })).toBeDefined()
    expect(await chat.find({ type: 'Text', text: /^weighing 399/ })).toBeUndefined()
    // Unfolded, the long output and thinking are far more than a drawing holds; what is drawn stays
    // well inside the engine's 100,000 characters (past them it drops elements and the desktop refuses
    // the tree).
    await chat.press({ key: 'fold-e5-h' })
    // Unfolded, the 140,000 characters of output are more than a drawing holds: the newest rows are
    // drawn, and the first message waits for a scroll to the top.
    await chat.press({ key: 'fold-e3-h' })
    expect(await chat.find({ type: 'Text', text: /^weighing 399/ })).toBeDefined()
    expect(await chat.find({ type: 'Markdown', text: /Build the wishlist API\./ })).toBeUndefined()
    expect(spent(await chat.drawn())).toBeLessThan(90_000)
    // The chat's switches fold all output and thinking again.
    await chat.press({ key: 'tools-codex-1' })
    await chat.press({ key: 'thinking-codex-1' })
    await chat.press({ key: 'thinking-codex-1' })
    expect(await chat.find({ type: 'Text', text: /^weighing 399/ })).toBeUndefined()
    expect(await chat.find({ type: 'Markdown', text: /Build the wishlist API\./ })).toBeDefined()
    await chat.unmount()

    for (const surface of ['terminal', 'desktop', 'vscode', 'mobile'] as const) {
      const ui = await $.ui.mount({ ...LIST, surface })
      const hasClient = surface === 'terminal' || surface === 'desktop'
      // Chats are listed by name (their task); archived ones only in the archive. Where the surface
      // draws a Client the list is the nav.tsx module, searched with `in`; elsewhere it is buttons.
      if (hasClient) {
        expect(await ui.find({ in: 'nav', text: /Build the wishlist API/ })).toBeDefined()
        expect(await ui.find({ in: 'nav', text: /Map the client/ })).toBeDefined()
        expect(await ui.find({ in: 'nav', text: /Map the API/ })).toBeUndefined()
        expect(await ui.find({ in: 'nav', text: /Archived \(1\)/ })).toBeDefined()
        // cursor-1 finished a turn nobody has looked at; codex-1 is working.
        expect(await ui.find({ in: 'nav', text: /●/ })).toBeDefined()
        expect(await ui.find({ in: 'nav', text: /[⠀-⣿]/ })).toBeDefined()
      } else {
        expect(await ui.find({ key: 'tab-cursor-1' })).toBeDefined()
        expect(await ui.find({ key: 'tab-antigravity-1' })).toBeUndefined()
        expect(await ui.find({ key: 'archived' })).toBeDefined()
      }
      if (hasClient) {
        // A right click on the chat opens its menu.
        await ui.pointer({ type: 'down', button: 'right', x: 4, y: 2, in: 'nav' })
        expect(await ui.find({ in: 'nav', key: 'menu-rename' })).toBeDefined()
        expect(await ui.find({ in: 'nav', key: 'menu-delete' })).toBeDefined()
        // Each item carries its icon.
        expect((await ui.find({ in: 'nav', key: 'menu-archive' }))?.text).toMatch(/⊟\s+Archive/)
        // Rename opens in the floating menu; a click outside closes it.
        await ui.press({ in: 'nav', key: 'menu-rename' })
        expect(await ui.find({ in: 'nav', key: 'rename-chat-codex-1' })).toBeDefined()
        await ui.pointer({ type: 'down', button: 'left', x: 2, y: 0, in: 'nav' })
        expect(await ui.find({ in: 'nav', key: 'rename-chat-codex-1' })).toBeUndefined()
        // A click on another chat opens it in a tab of its own, beside the first.
        await ui.pointer({ type: 'down', button: 'left', x: 4, y: 6, in: 'nav' })
        expect(open.get('chat-cursor-1')).toBe('◆ Map the client')
        expect(open.has('chat-codex-1')).toBe(true)
      }
      await ui.unmount()
    }
    // A second click on an open chat brings its tab forward: no second tab.
    expect(opened.filter(one => one.startsWith('chat-cursor-1')).length).toBeGreaterThan(1)
    expect(open.size).toBe(3)
  })
}
