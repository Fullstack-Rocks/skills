import { expect, test } from 'claude-code/testing'

// The pane drawn from a fake .delegate/ folder on every surface, in both layouts, so a tree a
// surface refuses (too many Select options, a key on a Text) fails here rather than in a session.
// The test's hooks stand in for the engine: the filesystem, the store, the clock and processes.

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
    { ts: 2, turn: 1, from: 'codex', kind: 'tool', text: '$ ls demo/app' },
    { ts: 3, turn: 1, from: 'codex', kind: 'tool_result', text: Array.from({ length: 200 }, (_, i) => `output line ${i} ${'·'.repeat(700)}`).join('\n') },
    { ts: 4, turn: 1, from: 'codex', kind: 'final', status: 'done', seconds: 9,
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

const PANE = {
  plugin: 'delegate',
  component: 'Pane',
  requestId: 'delegate',
  props: {
    title: 'Delegate',
    isFocused: false,
    bodyColumns: 100,
    placement: 'dock',
    scroll: { offset: 0, bodyRows: 60 },
    view: {},
  },
} as const

const missing = (path: string) => new Error(`ENOENT: ${path}`)

{
  test('the pane draws on every surface', { timeoutMs: 20000 }, async ($, on) => {
    on('session.start', (_, e) => ({ cwd: e.cwd }))
    on('session.root', () => ({ value: ROOT }))
    on('clock.every', () => ({ value: undefined }))
    on('command.register', () => ({ value: { command: 'delegations' } }))
    on('tool.register', () => ({ value: { tool: 'mcp__delegate__pane' } }))
    on('ui.open', () => ({ value: { isPlaced: true } }))
    on('ui.panes', () => ({ value: [] }))
    on('ui.status', () => ({ value: undefined }))
    on('store.get', () => ({ value: undefined }))
    let savedWidth: unknown
    on('store.set', (_, e) => {
      if (e.key === 'sidebar') savedWidth = e.value
      return { value: undefined }
    })
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

    for (const surface of ['terminal', 'desktop', 'vscode', 'mobile'] as const) {
      const ui = await $.ui.mount({ ...PANE, surface })
      const hasClient = surface === 'terminal' || surface === 'desktop'
      expect(await ui.find({ type: 'Text', text: /queued: Also add a docstring/ })).toBeDefined()
      // The pane scrolls the conversation natively. 140,000 characters of output are more than a drawing
      // holds, so the newest rows are drawn and the first message waits for a scroll to the top.
      expect(await ui.find({ type: 'Text', text: /output line 199/ })).toBeDefined()
      expect(await ui.find({ type: 'Markdown', text: /Build the wishlist API\./ })).toBeUndefined()
      // Replies are drawn as markdown.
      expect(await ui.find({ type: 'Markdown', text: /line 19/ })).toBeDefined()
      // At the newest end there is nothing below, so no "jump to the latest".
      expect(await ui.find({ key: 'latest' })).toBeUndefined()
      // Chats are listed by name (their task); archived ones only in the archive. Where the surface
      // draws a Client the list is the nav.tsx module, searched with `in`; elsewhere it is buttons.
      if (hasClient) {
        expect(await ui.find({ in: 'nav', text: /Build the wishlist API/ })).toBeDefined()
        expect(await ui.find({ in: 'nav', text: /Map the client/ })).toBeDefined()
        expect(await ui.find({ in: 'nav', text: /Map the API/ })).toBeUndefined()
        expect(await ui.find({ in: 'nav', text: /Archived \(1\)/ })).toBeDefined()
        // cursor-1 finished a turn nobody has looked at.
        expect(await ui.find({ in: 'nav', text: /●/ })).toBeDefined()
      } else {
        expect(await ui.find({ key: 'tab-cursor-1' })).toBeDefined()
        expect(await ui.find({ key: 'tab-antigravity-1' })).toBeUndefined()
        expect(await ui.find({ key: 'archived' })).toBeDefined()
      }
      // Model, effort and speed are separate pickers where the surface draws a Select (not mobile).
      if (surface !== 'mobile') {
        expect(await ui.find({ key: 'model-codex-1' })).toBeDefined()
        expect(await ui.find({ key: 'effort-codex-1' })).toBeDefined()
        expect(await ui.find({ key: 'speed-codex-1' })).toBeDefined()
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
        // Dragging the last column resizes the sidebar.
        await ui.pointer({ type: 'down', button: 'left', x: 29, y: 1, in: 'nav' })
        await ui.pointer({ type: 'move', button: 'left', x: 41, y: 1, in: 'nav' })
        await ui.pointer({ type: 'up', button: 'left', x: 41, y: 1, in: 'nav' })
        expect(savedWidth).toBe(46) // the list's 42 columns plus the panel's border and padding
      }
      await ui.unmount()
    }
  })
}
