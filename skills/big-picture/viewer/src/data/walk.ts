import type { LoadedGraph } from '../store/graph'
import type { GraphEdge } from '../types'

// Walks over the loaded graph, matching big-picture-query's scripts/graph/walk.py.
export const ENTRY_TYPES = new Set(['endpoint', 'job', 'cli'])
const ENTRY_KINDS = new Set(['calls', 'handled-by', 'reads', 'writes'])

export type Step = { step: number; edge: GraphEdge; id: string }

export function edgesOf(graph: LoadedGraph, id: string, direction: 'out' | 'in'): [GraphEdge, string][] {
  if (direction === 'out') return (graph.outgoing.get(id) ?? []).map((e) => [e, e.to])
  return (graph.incoming.get(id) ?? []).map((e) => [e, e.from])
}

/** Breadth-first steps up to `depth` away, following edges whose kind passes `keep`; each node once. */
export function neighbors(graph: LoadedGraph, id: string, depth: number, direction: 'out' | 'in',
  keep: (kind: string) => boolean): Step[] {
  const seen = new Set([id])
  const found: Step[] = []
  let frontier = [id]
  for (let step = 1; step <= depth && frontier.length; step++) {
    const next: string[] = []
    for (const current of frontier) {
      for (const [edge, other] of edgesOf(graph, current, direction)) {
        if (seen.has(other) || !keep(edge.kind)) continue
        seen.add(other)
        next.push(other)
        found.push({ step, edge, id: other })
      }
    }
    frontier = next
  }
  return found
}

export function entryPoints(graph: LoadedGraph, id: string): string[] {
  return neighbors(graph, id, 12, 'in', (kind) => ENTRY_KINDS.has(kind))
    .map((s) => s.id).filter((other) => ENTRY_TYPES.has(graph.byId.get(other)?.type ?? '')).sort()
}

/** Nodes reachable downstream (not through contains) that lead nowhere further: tables, leaf functions. */
export function leaves(graph: LoadedGraph, id: string): string[] {
  const downstream = (kind: string) => kind !== 'contains'
  return neighbors(graph, id, 12, 'out', downstream)
    .map((s) => s.id).filter((other) => !edgesOf(graph, other, 'out').some(([e]) => downstream(e.kind)))
}

/** The containers above a node, root first: the breadcrumb that reveals it. */
export function containersOf(graph: LoadedGraph, id: string): string[] {
  const chain: string[] = []
  for (let up = graph.parent.get(id); up; up = graph.parent.get(up)) chain.unshift(up)
  return chain
}

/** Nodes whose id or file-stem.name contains the text, exact names first (bp find's order). */
export function search(graph: LoadedGraph, text: string, limit: number): string[] {
  const needle = text.toLowerCase()
  const key = (id: string) => {
    const node = graph.byId.get(id)!
    const stem = node.file?.split('/').pop()?.replace(/\.[^.]+$/, '') ?? ''
    return `${node.id} ${stem}.${node.name}`.toLowerCase()
  }
  return [...graph.byId.keys()].filter((id) => key(id).includes(needle))
    .sort((a, b) => Number(graph.byId.get(a)!.name.toLowerCase() !== needle)
      - Number(graph.byId.get(b)!.name.toLowerCase() !== needle) || a.length - b.length)
    .slice(0, limit)
}
