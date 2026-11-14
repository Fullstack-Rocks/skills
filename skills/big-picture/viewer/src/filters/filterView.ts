import { DATABASE, frameOf } from '../data/layout'
import type { View, ViewEdge } from '../data/views'
import type { LoadedGraph } from '../store/graph'

// What the person hid to focus: node types, connection kinds and sections (the frames cards sit in:
// folders, modules, systems, capsules, the Database group). A section hides everything drawn inside it.
export type Hidden = { types: string[]; kinds: string[]; sections: string[] }
export type Contents = { types: Map<string, number>; kinds: Map<string, number>; sections: Map<string, number> }

const count = (counts: Map<string, number>, key: string) => counts.set(key, (counts.get(key) ?? 0) + 1)

/** The frames around a node in this view, innermost first. */
function framesAround(graph: LoadedGraph, view: View, id: string): string[] {
  const frames: string[] = []
  for (let up = frameOf(graph, view, id); up && !frames.includes(up); up = frameOf(graph, view, up)) frames.push(up)
  return frames
}

/** A connection's kinds: its members' when it rolls several up, else its own. */
function kindsOf(edge: ViewEdge): string[] {
  return edge.members.length ? edge.members.map((m) => m.kind) : [edge.kind]
}

/** What a view holds, for the filter pane: its node types, connection kinds and sections, with counts. */
export function viewContents(graph: LoadedGraph, view: View): Contents {
  const contents: Contents = { types: new Map(), kinds: new Map(), sections: new Map() }
  for (const id of view.nodes) {
    count(contents.types, graph.byId.get(id)?.type ?? 'other')
    for (const frame of framesAround(graph, view, id)) count(contents.sections, frame)
  }
  for (const edge of view.edges) for (const kind of new Set(kindsOf(edge))) count(contents.kinds, kind)
  return contents
}

/** A section's name: the folder, module, system or capsule it is, or the Database group. */
export function sectionName(graph: LoadedGraph, id: string): string {
  return id === DATABASE ? 'Database' : graph.byId.get(id)?.name ?? id.replace(/^group:/, '')
}

/** A rolled-up connection keeping only its members of shown kinds, relabelled; none when nothing is left. */
function keptEdge(edge: ViewEdge, hiddenKinds: Set<string>): ViewEdge | undefined {
  if (!edge.members.length) return hiddenKinds.has(edge.kind) ? undefined : edge
  const members = edge.members.filter((m) => !hiddenKinds.has(m.kind))
  if (!members.length) return undefined
  if (members.length === edge.members.length) return edge
  const kinds = new Map<string, number>()
  for (const m of members) count(kinds, m.kind)
  const label = [...kinds].map(([kind, n]) => (n > 1 ? `${kind} ×${n}` : kind)).join(' · ')
  return { ...edge, members, kind: [...kinds.keys()][0], label }
}

/** The view without what the person hid: nodes of hidden types or inside hidden sections, connections of hidden kinds. */
export function filterView(graph: LoadedGraph, view: View, hidden: Hidden): View {
  if (!hidden.types.length && !hidden.kinds.length && !hidden.sections.length) return view
  const [types, kinds, sections] = [new Set(hidden.types), new Set(hidden.kinds), new Set(hidden.sections)]
  const shown = new Set(view.nodes.filter((id) => !types.has(graph.byId.get(id)?.type ?? 'other')
    && !sections.has(id) && !framesAround(graph, view, id).some((frame) => sections.has(frame))))
  const edges = view.edges.filter((e) => shown.has(e.source) && shown.has(e.target))
    .flatMap((e) => keptEdge(e, kinds) ?? [])
  return { ...view, nodes: [...shown], edges }
}
