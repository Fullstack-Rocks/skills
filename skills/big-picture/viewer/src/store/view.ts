import { create } from 'zustand'

// What the person is doing: the node whose subgraph fills the canvas, how it is shown, and the
// node open in the pane. The URL hash mirrors `selected` (#/n/<id>). Edge style and direction are
// remembered in this browser.
export const ROOT = 'folder:.'

export type Mode = 'subgraph' | 'leaves'
export type EdgeStyle = 'default' | 'smoothstep' | 'step' | 'straight'
export type Direction = 'RIGHT' | 'DOWN' | 'LEFT' | 'UP'

const SETTINGS_KEY = 'big-picture.canvas'

type Settings = { edgeStyle: EdgeStyle; direction: Direction }

function storedSettings(): Settings {
  try {
    return { edgeStyle: 'default', direction: 'RIGHT', ...JSON.parse(localStorage.getItem(SETTINGS_KEY) ?? '{}') }
  } catch {
    return { edgeStyle: 'default', direction: 'RIGHT' }
  }
}

function storeSettings(settings: Settings): void {
  try { localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings)) } catch { /* private window */ }
}

type ViewState = Settings & {
  focus: string
  mode: Mode
  trail: string[] // focuses dived through, oldest first, for the breadcrumb
  selected: string | null
  select: (id: string | null) => void
  dive: (id: string, mode?: Mode) => void
  back: (index: number) => void
  reveal: (id: string, containers: string[]) => void
  setEdgeStyle: (edgeStyle: EdgeStyle) => void
  setDirection: (direction: Direction) => void
}

export const useView = create<ViewState>((set, get) => ({
  ...storedSettings(),
  focus: ROOT,
  mode: 'subgraph',
  trail: [],
  selected: null,
  select: (id) => set({ selected: id }),
  dive: (id, mode = 'subgraph') =>
    set((s) => (s.focus === id && s.mode === mode ? s : { focus: id, mode, trail: [...s.trail, s.focus] })),
  back: (index) => set((s) => ({ focus: s.trail[index], mode: 'subgraph', trail: s.trail.slice(0, index) })),
  // Show a node inside its container, with the containers above it as the breadcrumb (root first).
  reveal: (id, containers) =>
    set({ selected: id, focus: containers[containers.length - 1] ?? ROOT, mode: 'subgraph', trail: containers.slice(0, -1) }),
  setEdgeStyle: (edgeStyle) => { set({ edgeStyle }); storeSettings({ edgeStyle, direction: get().direction }) },
  setDirection: (direction) => { set({ direction }); storeSettings({ edgeStyle: get().edgeStyle, direction }) },
}))
