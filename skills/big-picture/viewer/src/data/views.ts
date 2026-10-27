import type { LoadedGraph } from '../store/graph'
import { ROOT, type Mode, type Tab } from '../store/view'
import type { GraphEdge, Lens } from '../types'
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
// heights: taller cards that list a table's columns (Database tab); flat: no folder or module frames;
// groups: frames other than folders and modules (a member's capsule).
export type View = { nodes: string[]; edges: ViewEdge[]; outside: Set<string>; heights?: Map<string, number>; flat?: boolean; groups?: Map<string, string> }

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

const API_KINDS = new Set(['implemented-by', 'handled-by', 'calls', 'reads', 'writes', 'looks-up', 'accepts', 'returns', 'has'])
const API_TYPES = new Set(['operation', 'endpoint'])

/** Every operation and endpoint, joined where the document and the code agree; or, focused on one,
 *  everything it runs and the models it takes and returns. */
function endpointsView(graph: LoadedGraph, focus: string): View {
  if (API_TYPES.has(graph.byId.get(focus)?.type ?? '')) {
    const shown = new Set([focus, ...neighbors(graph, focus, 7, 'out', (kind) => API_KINDS.has(kind)).map((s) => s.id)])
    return { nodes: [...shown], edges: edgesAmong(graph, shown), outside: new Set() }
  }
  const shown = new Set(graph.data.nodes.filter((n) => API_TYPES.has(n.type)).map((n) => n.id))
  return { nodes: [...shown], edges: edgesAmong(graph, shown), outside: new Set(), flat: true }
}

/** A view defined by a file: its node types, plus (with neighbors) whatever its connection kinds reach. */
function lensView(graph: LoadedGraph, lens: Lens): View {
  const types = new Set(lens.types)
  const follows = (kind: string) => (lens.edges ? lens.edges.includes(kind) : notContains(kind))
  const core = graph.data.nodes.filter((n) => types.has(n.type)).map((n) => n.id)
  const reached = lens.neighbors
    ? core.flatMap((id) => [...neighbors(graph, id, 1, 'in', follows), ...neighbors(graph, id, 1, 'out', follows)].map((s) => s.id))
    : []
  const shown = new Set([...core, ...reached])
  return { nodes: [...shown], edges: edgesAmong(graph, shown).filter((e) => follows(e.kind)), outside: new Set() }
}

/** Every capsule as a frame around its modules and tables, with what connects them rolled up. */
function capsulesView(graph: LoadedGraph): View {
  const groups = new Map(graph.data.edges.filter((e) => e.kind === 'groups').map((e) => [e.to, e.from]))
  const rolled = rollUp(graph, new Set(groups.keys()), (id) => id)
  return { nodes: [...groups.keys()], edges: rolled.edges.filter((e) => groups.has(e.source) && groups.has(e.target)), outside: new Set(), groups }
}

/** Every node with health findings of its own, in its folder and module frames (folders show theirs as frames). */
function healthView(graph: LoadedGraph): View {
  const shown = new Set([...graph.findings.keys()].filter((id) => graph.byId.has(id) && graph.byId.get(id)!.type !== 'folder'))
  return { nodes: [...shown], edges: edgesAmong(graph, shown), outside: new Set() }
}

export function visibleGraph(graph: LoadedGraph, focus: string, mode: Mode, tab: Tab): View {
  const lens = graph.data.views?.find((v) => v.id === tab)
  if (lens) return lensView(graph, lens)
  if (tab === 'capsules') return capsulesView(graph)
  if (tab === 'health') return healthView(graph)
  if (tab === 'database') return databaseView(graph)
  if (mode === 'leaves') return leavesView(graph, focus)
  return tab === 'endpoints' ? endpointsView(graph, focus) : mapView(graph, focus)
}

function mapView(graph: LoadedGraph, focus: string): View {
  const type = graph.byId.get(focus)?.type
  if (focus !== ROOT && type !== 'folder' && type !== 'module') return subgraphView(graph, focus)
  const units = new Set(unitsUnder(graph, focus))
  if (type === 'module') return rollUp(graph, units, (id) => id)
  // Outside a folder, code rolls up to its module, so the view stays at module level.
  return rollUp(graph, units, (id) => (CODE_INSIDE_MODULES.has(graph.byId.get(id)?.type ?? '') ? graph.parent.get(id) ?? id : id))
}
