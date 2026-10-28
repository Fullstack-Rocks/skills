import type { LoadedGraph } from '../store/graph'
import { ROOT, type Mode, type Tab } from '../store/view'
import type { GraphEdge, GraphNode, Lens } from '../types'
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

// contains and groups are membership (a folder's files, a capsule's modules), not connections to draw
const isConnection = (kind: string) => kind !== 'contains' && kind !== 'groups'
const CODE_INSIDE_MODULES = new Set(['function', 'endpoint'])
const MAX_UNITS = 300 // past this many modules a folder view shows its direct children instead

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
  if (units.length > MAX_UNITS) units.splice(0, units.length, ...(graph.children.get(focus) ?? []))
  // what no folder holds (a table, a topic), except capsules and systems, which have their own tabs
  const loose = (n: GraphNode) => !graph.parent.has(n.id) && n.id !== ROOT && n.type !== 'capsule' && n.type !== 'system'
  if (focus === ROOT) units.push(...graph.data.nodes.filter(loose).map((n) => n.id))
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
  for (const edge of graph.data.edges.filter((e) => isConnection(e.kind))) {
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
    .filter((e) => isConnection(e.kind) && shown.has(e.to))
    .map((e) => ({ id: `${e.from}|${e.kind}|${e.to}`, source: e.from, target: e.to, kind: e.kind, label: e.kind, approx: e.resolved === 'approx', members: [e] })))
}

function subgraphView(graph: LoadedGraph, focus: string): View {
  const steps = [...neighbors(graph, focus, 3, 'out', isConnection), ...neighbors(graph, focus, 2, 'in', isConnection)]
  const shown = new Set([focus, ...steps.map((s) => s.id)])
  // The walk crosses into other systems through their contracts; their side is drawn as outside.
  const home = graph.byId.get(focus)?.system
  const outside = new Set([...shown].filter((id) => home && graph.byId.get(id)?.system && graph.byId.get(id)!.system !== home))
  return { nodes: [...shown], edges: edgesAmong(graph, shown), outside }
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
  // a frame per database schema (crm, tasks, ...) when the DDL names any; unnamed tables share a default one
  const named = [...shown].some((id) => graph.byId.get(id)?.schema)
  const tables = [...shown].filter((id) => graph.byId.get(id)?.type === 'table')
  const groups = new Map(named ? tables.map((id) => [id, `group:${graph.byId.get(id)?.schema ?? 'default'} schema`]) : [])
  return { nodes: [...shown], edges, outside: new Set(), heights, flat: true, ...(groups.size ? { groups } : {}) }
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
  const follows = (kind: string) => (lens.edges ? lens.edges.includes(kind) : isConnection(kind))
  const core = graph.data.nodes.filter((n) => types.has(n.type)).map((n) => n.id)
  const reached = lens.neighbors
    ? core.flatMap((id) => [...neighbors(graph, id, 1, 'in', follows), ...neighbors(graph, id, 1, 'out', follows)].map((s) => s.id))
    : []
  const shown = new Set([...core, ...reached])
  return { nodes: [...shown], edges: edgesAmong(graph, shown).filter((e) => follows(e.kind)), outside: new Set() }
}

/** Every capsule as a frame around its modules and tables, with what connects them rolled up. Past
 * MAX_UNITS members each capsule is one card linked to the others; diving into one shows its members. */
function capsulesView(graph: LoadedGraph, focus: string): View {
  if (focus !== ROOT && graph.byId.get(focus)?.type !== 'capsule') return subgraphView(graph, focus)
  const all = graph.data.edges.filter((e) => e.kind === 'groups' && (focus === ROOT || e.from === focus))
  const groups = new Map(all.map((e) => [e.to, e.from]))
  const edges = rollUp(graph, new Set(groups.keys()), (id) => id).edges.filter((e) => groups.has(e.source) && groups.has(e.target))
  if (groups.size <= MAX_UNITS) return { nodes: [...groups.keys()], edges, outside: new Set(), groups }
  return { nodes: [...new Set(groups.values())], edges: capsuleLinks(edges, groups), outside: new Set() }
}

/** Member-to-member connections rolled up to one edge per pair of capsules. */
function capsuleLinks(edges: ViewEdge[], capsuleOf: Map<string, string>): ViewEdge[] {
  const pairs = new Map<string, ViewEdge>()
  for (const edge of edges) {
    const [source, target] = [capsuleOf.get(edge.source)!, capsuleOf.get(edge.target)!]
    const id = `${source}|${target}`
    if (source === target) continue
    const pair = pairs.get(id) ?? { id, source, target, kind: edge.kind, label: '', approx: false, members: [] }
    pair.members.push(...edge.members)
    pair.approx ||= edge.approx
    pairs.set(id, pair)
  }
  return [...pairs.values()].map((pair) => ({ ...pair, label: kindCounts(pair.members) }))
}

function kindCounts(members: GraphEdge[]): string {
  const counts = new Map<string, number>()
  for (const edge of members) counts.set(edge.kind, (counts.get(edge.kind) ?? 0) + 1)
  return [...counts].map(([kind, count]) => (count > 1 ? `${kind} ×${count}` : kind)).join(' · ')
}

/** The other end of a connection, when it lies in another system or is a contract several systems share. */
export function crossesTo(graph: LoadedGraph, id: string, other: string): boolean {
  const [mine, theirs] = [graph.byId.get(id)?.system, graph.byId.get(other)?.system]
  return Boolean(mine) && (theirs ? theirs !== mine : graph.shared.has(other))
}

export type Port = { id: string; kind: string; label: string }

/** A card's connections into other systems or shared contracts: its ports, shown as badges, not long wires. */
export function portsOf(graph: LoadedGraph, id: string): Port[] {
  const out = (graph.outgoing.get(id) ?? []).map((e): [string, string] => [e.kind, e.to])
  const into = (graph.incoming.get(id) ?? []).map((e): [string, string] => [e.kind, e.from])
  return [...out, ...into].filter(([kind, other]) => isConnection(kind) && crossesTo(graph, id, other))
    .map(([kind, other]) => ({ id: other, kind, label: portLabel(graph, kind, other) }))
}

function portLabel(graph: LoadedGraph, kind: string, other: string): string {
  const node = graph.byId.get(other)
  const where = node?.system ? ' · ' + node.system : ''
  return kind + ' ' + (node?.name ?? other) + where
}

/** Each system as a frame holding only its boundary code, with the contracts between the frames. Past
 * MAX_UNITS boundary nodes, each is lifted to its module and only the crossings are rolled up between them. */
function systemsView(graph: LoadedGraph): View {
  const boundary = graph.data.edges.filter((e) => isConnection(e.kind)).flatMap((e) => [
    ...(crossesTo(graph, e.from, e.to) ? [e.from] : []), ...(crossesTo(graph, e.to, e.from) ? [e.to] : []),
  ])
  const detail = new Set([...boundary, ...graph.shared])
  const lifted = detail.size > MAX_UNITS
  const shown = lifted ? new Set([...detail].map((id) => moduleOf(graph, id))) : detail
  const groups = new Map([...shown].flatMap((id) => (graph.byId.get(id)?.system ? [[id, `system:${graph.byId.get(id)!.system}`] as [string, string]] : [])))
  const crossing = (e: ViewEdge) => shown.has(e.source) && shown.has(e.target) && (crossesTo(graph, e.source, e.target) || crossesTo(graph, e.target, e.source))
  const edges = lifted ? rollUp(graph, shown, (id) => id).edges.filter(crossing) : edgesAmong(graph, shown)
  return { nodes: [...shown], edges, outside: new Set(), groups }
}

/** The module a function or endpoint lives in; anything else is its own unit. */
function moduleOf(graph: LoadedGraph, id: string): string {
  return CODE_INSIDE_MODULES.has(graph.byId.get(id)?.type ?? '') ? graph.parent.get(id) ?? id : id
}

/** Every node with health findings of its own, in its folder and module frames (folders show theirs as frames). */
function healthView(graph: LoadedGraph): View {
  const shown = new Set([...graph.findings.keys()].filter((id) => graph.byId.has(id) && graph.byId.get(id)!.type !== 'folder'))
  return { nodes: [...shown], edges: edgesAmong(graph, shown), outside: new Set() }
}

export function visibleGraph(graph: LoadedGraph, focus: string, mode: Mode, tab: Tab): View {
  const lens = graph.data.views?.find((v) => v.id === tab)
  if (lens) return lensView(graph, lens)
  if (tab === 'capsules') return capsulesView(graph, focus)
  if (tab === 'systems') return systemsView(graph)
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
