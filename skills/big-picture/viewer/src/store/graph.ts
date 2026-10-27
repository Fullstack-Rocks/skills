import { create } from 'zustand'

import { setCustomColors } from '../theme'
import type { Finding, GraphData, GraphEdge, GraphNode } from '../types'

// What was loaded, with the indexes every view needs, built once per load.
export type LoadedGraph = {
  data: GraphData
  byId: Map<string, GraphNode>
  outgoing: Map<string, GraphEdge[]>
  incoming: Map<string, GraphEdge[]>
  parent: Map<string, string> // the node that contains this one
  children: Map<string, string[]>
  findings: Map<string, Finding[]>
  health: Map<string, number> // findings on the node and everything it contains
  shared: Set<string> // contracts: nodes in no system that two or more systems use (a topic, a socket message)
}

type GraphState = {
  graph: LoadedGraph | null
  live: boolean // served by serve.py, so source files and rebuilds are reachable
  error: string | null
  setGraph: (data: GraphData, live: boolean) => void
  setError: (error: string) => void
}

function push<T>(map: Map<string, T[]>, key: string, value: T): void {
  const list = map.get(key)
  if (list) list.push(value)
  else map.set(key, [value])
}

function totalHealth(graph: LoadedGraph, id: string): number {
  const own = graph.findings.get(id)?.length ?? 0
  const kids = graph.children.get(id) ?? []
  const total = kids.reduce((sum, kid) => sum + totalHealth(graph, kid), own)
  graph.health.set(id, total)
  return total
}

/** Remember which systems use a node that belongs to none (the contract between them). */
function noteUser(graph: LoadedGraph, users: Map<string, Set<string>>, edge: GraphEdge): void {
  const [a, b] = [graph.byId.get(edge.from)?.system, graph.byId.get(edge.to)?.system]
  if (edge.kind === 'contains' || Boolean(a) === Boolean(b)) return
  const [contract, system] = a ? [edge.to, a] : [edge.from, b!]
  users.set(contract, (users.get(contract) ?? new Set()).add(system))
}

export function indexGraph(data: GraphData): LoadedGraph {
  const graph: LoadedGraph = {
    data, byId: new Map(data.nodes.map((n) => [n.id, n])), outgoing: new Map(), incoming: new Map(),
    parent: new Map(), children: new Map(), findings: new Map(), health: new Map(), shared: new Set(),
  }
  const users = new Map<string, Set<string>>()
  for (const edge of data.edges) {
    push(graph.outgoing, edge.from, edge)
    push(graph.incoming, edge.to, edge)
    if (edge.kind === 'contains') {
      graph.parent.set(edge.to, edge.from)
      push(graph.children, edge.from, edge.to)
    }
    noteUser(graph, users, edge)
  }
  for (const [id, systems] of users) if (systems.size > 1) graph.shared.add(id)
  for (const finding of data.findings) push(graph.findings, finding.node, finding)
  for (const node of data.nodes) if (!graph.parent.has(node.id)) totalHealth(graph, node.id)
  return graph
}

export const useGraph = create<GraphState>((set) => ({
  graph: null,
  live: false,
  error: null,
  setGraph: (data, live) => {
    setCustomColors(Object.assign({}, ...(data.views ?? []).map((v) => v.colors)))
    set({ graph: indexGraph(data), live, error: null })
  },
  setError: (error) => set({ error }),
}))
