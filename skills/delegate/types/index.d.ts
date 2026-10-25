// One line of .delegate/<id>/events.jsonl, as scripts/delegate.py writes it.
export type DelegateEvent = {
  ts: number
  turn: number
  from: string
  kind: 'message' | 'thinking' | 'tool' | 'tool_result' | 'error' | 'status' | 'final'
  text: string
  status?: string
  seconds?: number
  attachments?: string[]
}

// What the pane draws of .delegate/<id>/state.json, plus how the person filed it (meta.json).
export type Delegation = {
  id: string
  harness: string
  status: string
  agentStatus: string
  mode: string
  turns: number
  title: string
  name: string
  model: string
  effort: string
  speed: string
  created: number
  archived: boolean
  project: string
  seenTurns: number
}

// One model a harness offers, from `delegate.py models <harness> --json`, with the efforts and
// speeds it takes (empty when the harness has no such choice).
export type ModelOption = { id: string; label: string; efforts: string[]; speeds: string[] }

// One entry of assets/brands.json.
export type Brand = { name: string; color: string; glyph: string; svg: string }

// A message waiting in .delegate/<id>/queue.jsonl for the running turn to end.
export type QueuedMessage = { from: string; text: string; attachments: string[]; ts: number }

// What hooks/nav.tsx (the chat list's surface module) draws, and what it posts back.
export type NavChat = { id: string; name: string; glyph: string; color: string; running: boolean; unread: boolean }
export type NavProps = {
  width: number
  hoverColor: string
  selected: string
  archived: number
  groups: { project: string; chats: NavChat[] }[]
}
export type NavAction =
  | { type: 'none' }
  | { type: 'resize'; width: number }
  | { type: 'select' | 'archive' | 'delete'; target: string }
  | { type: 'rename' | 'rename-project'; target: string; value: string }

declare module 'claude-code' {
  interface PluginState {
    delegate: {
      delegations: Delegation[]
      selected: string
      page: { start: number; end: number; total: number }
      scroll: number
      sending: string
      models: Record<string, ModelOption[]>
      naming: string
      drafts: Record<string, string>
      attachments: Record<string, string[]>
      queue: QueuedMessage[]
      sidebar: number
      extra: number
      layers: number
    }
  }
}
