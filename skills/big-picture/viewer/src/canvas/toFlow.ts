import { MarkerType, type Edge } from '@xyflow/react'

import { subtitle } from '../data/describe'
import { DATABASE, type Placed } from '../data/layout'
import type { View } from '../data/views'
import type { LoadedGraph } from '../store/graph'
import type { Direction, EdgeStyle } from '../store/view'
import { edgeColor, theme } from '../theme'
import type { CardNode } from './NodeCard'
import type { GroupNode } from './frames/GroupCard'

export type FlowNode = CardNode | GroupNode

function groupNode(graph: LoadedGraph, p: Placed): GroupNode {
  const node = graph.byId.get(p.id)
  const database = p.id === DATABASE
  const data = { label: node?.name ?? (database ? 'Database' : p.id), type: node?.type ?? (database ? 'database' : 'group'), health: graph.health.get(p.id) ?? 0, selected: false }
  return { id: p.id, type: 'group', parentId: p.parent, position: { x: p.x, y: p.y }, width: p.width, height: p.height, data, selectable: p.id !== DATABASE }
}

/** The edge kinds arriving at and leaving each shown node, in a stable order. */
function kindsBySide(view: View): Sides {
  const into = new Map<string, Set<string>>()
  const out = new Map<string, Set<string>>()
  for (const e of view.edges) {
    into.set(e.target, (into.get(e.target) ?? new Set()).add(e.kind))
    out.set(e.source, (out.get(e.source) ?? new Set()).add(e.kind))
  }
  const sorted = (sides: Map<string, Set<string>>) => new Map([...sides].map(([id, kinds]) => [id, [...kinds].sort()]))
  return { into: sorted(into), out: sorted(out) }
}

type Sides = { into: Map<string, string[]>; out: Map<string, string[]> }
type Context = { view: View; sides: Sides; focus: string; direction: Direction }

/** A card's data apart from its subtitle: health, focus, its connection dots and, in the Database tab, its rows. */
function cardData(graph: LoadedGraph, p: Placed, { view, sides, focus, direction }: Context) {
  const node = graph.byId.get(p.id)!
  return {
    node, health: graph.health.get(p.id) ?? 0, focused: p.id === focus, selected: false, outside: view.outside.has(p.id),
    inKinds: sides.into.get(p.id) ?? [], outKinds: sides.out.get(p.id) ?? [], direction,
    columns: view.heights ? node.columns ?? [] : undefined, height: view.heights?.get(p.id),
  }
}

/** React Flow nodes from a layout: groups as frames, everything else as cards. */
export function toFlowNodes(graph: LoadedGraph, placed: Placed[], view: View, focus: string, direction: Direction): FlowNode[] {
  const sides = kindsBySide(view)
  return placed.map((p): FlowNode => {
    const node = graph.byId.get(p.id)
    if (p.group || !node) return groupNode(graph, p)
    const data = { ...cardData(graph, p, { view, sides, focus, direction }), subtitle: subtitle(graph, node) }
    return { id: p.id, type: 'card', parentId: p.parent, position: { x: p.x, y: p.y }, data }
  })
}

/** Edges drawn in the person's style, each from its kind's dot to its kind's dot. */
export function toFlowEdges(view: View, edgeStyle: EdgeStyle): Edge[] {
  return view.edges.map((e) => ({
    id: e.id, source: e.source, target: e.target, label: e.label, data: { color: edgeColor(e.kind), members: e.members }, type: edgeStyle,
    sourceHandle: `out-${e.kind}`, targetHandle: `in-${e.kind}`,
    labelStyle: { fill: theme.text, fontSize: 11 }, labelBgStyle: { fill: theme.bg, fillOpacity: 0.92 },
    labelBgPadding: [6, 3] as [number, number], labelBgBorderRadius: 4,
    style: { stroke: edgeColor(e.kind), strokeWidth: 1.8, strokeDasharray: e.approx ? '5 4' : undefined },
    markerEnd: { type: MarkerType.ArrowClosed, color: edgeColor(e.kind) },
  }))
}

/** With a node or group selected, its edges in both directions (and those of everything inside a
 *  selected group) animate in front at full strength; with a connection selected, only it does. The
 *  rest fade back. */
export function highlightEdges(edges: Edge[], nodes: FlowNode[], selected: string | null, selectedEdge: string | null): Edge[] {
  if (!selected && !selectedEdge) return edges
  const parentOf = new Map(nodes.map((n) => [n.id, n.parentId]))
  const related = (id: string) => {
    for (let up: string | undefined = id; up; up = parentOf.get(up)) if (up === selected) return true
    return false
  }
  return edges.map((e) => {
    const on = selectedEdge ? e.id === selectedEdge : related(e.source) || related(e.target)
    return {
      ...e, animated: on,
      style: { ...e.style, strokeWidth: on ? 2.6 : 1.2, opacity: on ? 1 : 0.15 },
      labelStyle: { ...e.labelStyle, fill: on ? String(e.data?.color) : theme.muted, fontWeight: on ? 700 : 400, opacity: on ? 1 : 0.3 },
      labelBgStyle: { ...e.labelBgStyle, fillOpacity: on ? 0.95 : 0.3 },
    }
  })
}
