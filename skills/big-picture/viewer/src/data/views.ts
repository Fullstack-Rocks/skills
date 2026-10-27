import type { LoadedGraph } from '../store/graph'
import { ROOT, type Mode, type Tab } from '../store/view'
import type { GraphEdge } from '../types'
import { leaves, neighbors } from './walk'

// The nodes and edges the canvas shows for a focus:
//  - the project or a folder: every module and file under it (the birds-eye view), with the calls,
//    reads and writes between them rolled up per pair ("calls ×12 · reads"), plus the modules and
//    tables outside it that they talk to
//  - a module: its functions and endpoints with every function, endpoint and table they use or
//    are used by, edge by edge (the usage graph)
//  - any other node: what it reaches downstream (3 steps) and what reaches it (2 steps)
//  - leaves mode: the node and the terminal nodes it reaches, one edge each
//  - the Database tab: every table, view and JSON lookup, with how they reference each other
// layout.ts groups the nodes by folder and module. Each shown edge keeps the graph edges it stands for.
export type ViewEdge = { id: string; source: string; target: string; kind: string; label: string; approx: boolean; members: GraphEdge[] }
// heights: taller cards that list a table's columns (Database tab); flat: no folder or module frames.
export type View = { nodes: string[]; edges: ViewEdge[]; outside: Set<string>; heights?: Map<string, number>; flat?: boolean }

const notContains = (kind: string) => kind !== 'contains'
const CODE_INSIDE_MODULES = new Set(['function', 'endpoint'])

/** The project's or folder's modules and files, through subfolders; a module's own functions and endpoints. */
function unitsUnder(graph: LoadedGraph, focus: string): string[] {
  const units: string[] = []
  const visit = (id: string) => {
    for (const child of graph.children.get(id) ?? []) {
      if (graph.byId.get(child)?.type === 'folder') visit(child)
      else units.push(child)
    }
  }
  if (graph.byId.get(focus)?.type === 'module') return [...(graph.children.get(focus) ?? [])]
  visit(focus)
  if (focus === ROOT) units.push(...graph.data.nodes.filter((n) => !graph.parent.has(n.id) && n.id !== ROOT).map((n) => n.id))
  return units
}

/** One edge per pair, from every edge with at least one end inside; outside ends shown at `outsideLevel`. */
function rollUp(graph: LoadedGraph, units: Set<string>, outsideLevel: (id: string) => string): View {
  const inside = (id: string): string | undefined => {
    let up: string | undefined = id
    while (up && !units.has(up)) up = graph.parent.get(up)
    return up
  }
  const pairs = new Map<string, { source: string; target: string; kinds: Map<string, number>; approx: boolean; members: GraphEdge[] }>()
  const outside = new Set<string>()
  for (const edge of graph.data.edges.filter((e) => notContains(e.kind))) {
    const [from, to] = [inside(edge.from), inside(edge.to)]
    const [source, target] = [from ?? outsideLevel(edge.from), to ?? outsideLevel(edge.to)]
    if ((!from && !to) || source === target) continue
    if (!from) outside.add(source)
    if (!to) outside.add(target)
    const pair = pairs.get(`${source}|${target}`) ?? { source, target, kinds: new Map(), approx: false, members: [] as GraphEdge[] }
    pair.kinds.set(edge.kind, (pair.kinds.get(edge.kind) ?? 0) + 1)
    pair.members.push(edge)
    pair.approx ||= edge.resolved === 'approx'
    pairs.set(`${source}|${target}`, pair)
  }
  const edges = [...pairs].map(([id, { source, target, kinds, approx, members }]) => ({
    id, source, target, approx, members, kind: [...kinds.keys()][0],
    label: [...kinds].map(([kind, count]) => (count > 1 ? `${kind} ×${count}` : kind)).join(' · '),
  }))
  return { nodes: [...units, ...outside], edges, outside }
}

/** Every edge (not contains) whose two ends are both shown. */
function edgesAmong(graph: LoadedGraph, shown: Set<string>): ViewEdge[] {
  return [...shown].flatMap((id) => (graph.outgoing.get(id) ?? [])
    .filter((e) => notContains(e.kind) && shown.has(e.to))
    .map((e) => ({ id: `${e.from}|${e.kind}|${e.to}`, source: e.from, target: e.to, kind: e.kind, label: e.kind, approx: e.resolved === 'approx', members: [e] })))
}

function subgraphView(graph: LoadedGraph, focus: string): View {
  const steps = [...neighbors(graph, focus, 3, 'out', notContains), ...neighbors(graph, focus, 2, 'in', notContains)]
  const shown = new Set([focus, ...steps.map((s) => s.id)])
  return { nodes: [...shown], edges: edgesAmong(graph, shown), outside: new Set() }
}

function leavesView(graph: LoadedGraph, focus: string): View {
  const ends = leaves(graph, focus)
  const edges = ends.map((end) => ({ id: `${focus}|reaches|${end}`, source: focus, target: end, kind: 'reaches', label: 'reaches', approx: false, members: [] }))
  return { nodes: [focus, ...ends], edges, outside: new Set() }
}

const DATABASE_KINDS = new Set(['references', 'selects-from', 'through', 'finds'])
export const TABLE_HEAD = 66
export const TABLE_ROW = 20

function databaseView(graph: LoadedGraph): View {
  const shown = new Set(graph.data.nodes.filter((n) => n.type === 'table' || n.type === 'lookup').map((n) => n.id))
  const edges = edgesAmong(graph, shown).filter((e) => DATABASE_KINDS.has(e.kind))
  const heights = new Map([...shown].map((id) => [id, TABLE_HEAD + TABLE_ROW * Math.max(graph.byId.get(id)?.columns?.length ?? 0, 1)]))
  return { nodes: [...shown], edges, outside: new Set(), heights, flat: true }
}

export function visibleGraph(graph: LoadedGraph, focus: string, mode: Mode, tab: Tab): View {
  if (tab === 'database') return databaseView(graph)
  if (mode === 'leaves') return leavesView(graph, focus)
  const type = graph.byId.get(focus)?.type
  if (focus !== ROOT && type !== 'folder' && type !== 'module') return subgraphView(graph, focus)
  const units = new Set(unitsUnder(graph, focus))
  if (type === 'module') return rollUp(graph, units, (id) => id)
  // Outside a folder, code rolls up to its module, so the view stays at module level.
  return rollUp(graph, units, (id) => (CODE_INSIDE_MODULES.has(graph.byId.get(id)?.type ?? '') ? graph.parent.get(id) ?? id : id))
}
