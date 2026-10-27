import ELK, { type ElkExtendedEdge, type ElkNode } from 'elkjs/lib/elk.bundled.js'

import type { LoadedGraph } from '../store/graph'
import { ROOT, type Direction } from '../store/view'
import type { View } from './views'

// Nested layout: functions sit inside their module, modules inside their folders, tables inside a
// Database group. Each group is laid out on its own: layered left to right when its members connect,
// packed into a grid when they don't, flowing in the direction the person picked. An edge between groups is lifted to the level where it
// crosses, so groups line up by how they call each other, with room reserved for its label.
export const NODE_WIDTH = 260
export const NODE_HEIGHT = 78
export const DATABASE = 'group:database'

export type Placed = { id: string; parent?: string; x: number; y: number; width: number; height: number; group: boolean }

const elk = new ELK()
const LAYERED = {
  'elk.algorithm': 'layered',
  'elk.direction': 'RIGHT',
  'elk.layered.spacing.nodeNodeBetweenLayers': '110',
  'elk.layered.spacing.edgeNodeBetweenLayers': '36',
  'elk.layered.nodePlacement.strategy': 'NETWORK_SIMPLEX',
  'elk.spacing.nodeNode': '24',
  'elk.spacing.edgeLabel': '8',
  'elk.spacing.componentComponent': '48',
  'elk.edgeLabels.placement': 'CENTER',
}
const PACKED = { 'elk.algorithm': 'rectpacking', 'elk.aspectRatio': '1.6', 'elk.spacing.nodeNode': '20' }
const PADDING = { 'elk.padding': '[top=48,left=20,bottom=20,right=20]' }

/** The group a node is drawn inside: its container (not the project root), or Database for tables. */
export function groupOf(graph: LoadedGraph, id: string): string | undefined {
  if (graph.byId.get(id)?.type === 'table') return DATABASE
  const parent = graph.parent.get(id)
  return parent === ROOT ? undefined : parent
}

/** The nested ELK nodes for a view, and each node's holder ('root' at the top). */
type Tree = { made: Map<string, ElkNode>; holderOf: Map<string, string> }

function elkTree(graph: LoadedGraph, view: View): Tree {
  const made = new Map<string, ElkNode>([['root', { id: 'root', children: [] }]])
  const holderOf = new Map<string, string>()
  for (const id of view.nodes) {
    // The node and the groups above it that don't exist yet, outermost first.
    const chain = [id]
    const group = (node: string) => (view.flat ? undefined : groupOf(graph, node))
    for (let up = group(id); up && !made.has(up); up = group(up)) chain.unshift(up)
    let holder = group(chain[0]) ?? 'root'
    for (const member of chain) {
      if (!made.has(member)) {
        // Every node starts with an empty children list, so any of them can hold members.
        const height = view.heights?.get(id) ?? NODE_HEIGHT
        const node: ElkNode = member === id ? { id, width: NODE_WIDTH, height, children: [] } : { id: member, children: [] }
        made.get(holder)!.children!.push(node)
        made.set(member, node)
        holderOf.set(member, holder)
      }
      holder = member
    }
  }
  return { made, holderOf }
}

/** Each view edge as an edge between the two members of the group where it crosses, keyed by that group. */
function liftedEdges(view: View, holderOf: Map<string, string>): Map<string, ElkExtendedEdge[]> {
  const chainOf = (id: string) => {
    const chain = [id]
    for (let up = holderOf.get(id); up; up = holderOf.get(up)) chain.push(up)
    return chain
  }
  const lifted = new Map<string, Map<string, ElkExtendedEdge>>()
  for (const edge of view.edges) {
    const [from, to] = [chainOf(edge.source), chainOf(edge.target)]
    const shared = from.findIndex((id, i) => i > 0 && to.includes(id))
    const [source, target] = [from[shared - 1], to[to.indexOf(from[shared]) - 1]]
    if (shared < 0 || !source || !target || source === target) continue
    const level = lifted.get(from[shared]) ?? new Map<string, ElkExtendedEdge>()
    const label = { text: edge.label, width: edge.label.length * 6.6 + 12, height: 18 }
    const known = level.get(`${source}|${target}`)
    if (!known || known.labels![0].width! < label.width) level.set(`${source}|${target}`, { id: `${source}|${target}`, sources: [source], targets: [target], labels: [label] })
    lifted.set(from[shared], level)
  }
  return new Map([...lifted].map(([group, edges]) => [group, [...edges.values()]]))
}

/** Every node and group with its position relative to its group; groups come before their members. */
export async function elkLayout(graph: LoadedGraph, view: View, direction: Direction): Promise<Placed[]> {
  const { made, holderOf } = elkTree(graph, view)
  const edges = liftedEdges(view, holderOf)
  for (const [id, node] of made) {
    if (!node.children?.length) continue
    node.edges = edges.get(id) ?? []
    const layered = { ...LAYERED, 'elk.direction': direction }
    node.layoutOptions = { ...(node.edges.length ? layered : PACKED), ...(id === 'root' ? {} : PADDING) }
  }
  const laid = await elk.layout(made.get('root')!)
  const placed: Placed[] = []
  const walk = (node: ElkNode, parent?: string) => {
    const { id, x = 0, y = 0, width = NODE_WIDTH, height = NODE_HEIGHT, children } = node
    placed.push({ id, parent, x, y, width, height, group: Boolean(children?.length) })
    for (const child of children ?? []) walk(child, id)
  }
  for (const child of laid.children ?? []) walk(child)
  return placed
}
