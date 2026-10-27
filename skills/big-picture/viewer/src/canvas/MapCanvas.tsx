import { applyNodeChanges, Background, Controls, ReactFlow, useNodesState, useReactFlow, type Edge, type NodeChange } from '@xyflow/react'
import '@xyflow/react/dist/style.css'
import { useEffect, useMemo, useState } from 'react'
import styled from 'styled-components'

import { elkLayout } from '../data/layout'
import { visibleGraph } from '../data/views'
import { Breadcrumb } from '../nav/Breadcrumb'
import { useGraph } from '../store/graph'
import { useView } from '../store/view'
import { theme } from '../theme'
import type { GraphEdge } from '../types'
import { GroupCard } from './GroupCard'
import { Toolbar } from './Toolbar'
import { NodeCard } from './NodeCard'
import { arrange, settle } from './settle'
import { highlightEdges, toFlowEdges, toFlowNodes, type FlowNode } from './toFlow'

const NODE_TYPES = { card: NodeCard, group: GroupCard }

const Area = styled.main`
  position: relative; min-width: 0; min-height: 0;
  .react-flow { background: ${theme.bg}; }
  .react-flow__node-group { padding: 0; border: 0; background: none; box-shadow: none; }
  .react-flow__controls button { background: ${theme.panel}; border-color: ${theme.border}; fill: ${theme.text}; }
`
const Status = styled.div`position: absolute; inset: 0; display: grid; place-items: center; color: ${theme.muted};`

/** Zooms to a clicked connection's two ends. */
function FocusEdge() {
  const { fitView } = useReactFlow()
  const edge = useView((s) => s.selectedEdge)
  useEffect(() => {
    if (edge) void fitView({ nodes: [{ id: edge.source }, { id: edge.target }], duration: 400, padding: 0.4, maxZoom: 1.2 })
  }, [edge, fitView])
  return null
}

export function MapCanvas() {
  const graph = useGraph((s) => s.graph)
  const { focus, mode, selected, selectedEdge, select, selectEdge, dive, direction, edgeStyle, tab } = useView()
  const [nodes, setNodes] = useNodesState<FlowNode>([])
  const [baseEdges, setEdges] = useState<Edge[]>([])
  const edges = useMemo(() => highlightEdges(baseEdges, nodes, selected, selectedEdge?.id ?? null).map((e): Edge => ({ ...e, type: edgeStyle })),
    [baseEdges, nodes, selected, selectedEdge, edgeStyle])
  // A focused connection dims every card but its two ends.
  const ends = selectedEdge
  const shown = useMemo(() => nodes.map((n): FlowNode => (n.type === 'card'
    ? (ends ? { ...n, data: { ...n.data, dimmed: n.id !== ends.source && n.id !== ends.target } } : n)
    : { ...n, data: { ...n.data, onArrange: (id: string, columns: number) => setNodes((all) => arrange(all, id, columns)) } })),
  [nodes, ends, setNodes])

  // Dragging pushes overlapping cards on the same level and grows the frames around them.
  const onNodesChange = (changes: NodeChange<FlowNode>[]) => setNodes((current) => {
    const next = applyNodeChanges(changes, current)
    const drag = changes.find((c) => c.type === 'position' && c.dragging && c.position)
    if (!drag || drag.type !== 'position') return next
    const before = current.find((n) => n.id === drag.id)!.position
    return settle(next, drag.id, drag.position!.x - before.x, drag.position!.y - before.y)
  })
  const [layoutId, setLayoutId] = useState(0) // remounts the flow after each layout so it fits the view

  useEffect(() => {
    if (!graph) return
    let current = true
    const view = visibleGraph(graph, focus, mode, tab)
    void elkLayout(graph, view, direction).then((placed) => {
      if (!current) return
      setNodes(toFlowNodes(graph, placed, view, focus, direction))
      setEdges(toFlowEdges(view, useView.getState().edgeStyle))
      setLayoutId((n) => n + 1)
    })
    return () => { current = false }
  }, [graph, focus, mode, direction, tab, setNodes])

  // Selection only restyles; it keeps positions the person dragged.
  useEffect(() => {
    setNodes((all) => all.map((n) => (n.data.selected === (n.id === selected) ? n : { ...n, data: { ...n.data, selected: n.id === selected } } as FlowNode)))
  }, [selected, layoutId, setNodes])

  return (
    <Area>
      {tab === 'map' && <Breadcrumb />}
      <Toolbar />
      {layoutId === 0 && <Status>Laying out the graph…</Status>}
      <ReactFlow key={layoutId} nodes={shown} edges={edges} nodeTypes={NODE_TYPES} onNodesChange={onNodesChange}
        onEdgeClick={(_, e) => selectEdge({ id: e.id, source: e.source, target: e.target, label: String(e.label), members: (e.data?.members ?? []) as GraphEdge[] })}
        fitView fitViewOptions={{ maxZoom: 1, padding: 0.08 }} minZoom={0.05} zoomOnDoubleClick={false}
        nodesConnectable={false} proOptions={{ hideAttribution: true }}
        onNodeClick={(_, n) => select(n.id)} onNodeDoubleClick={(_, n) => tab === 'map' && n.id !== focus && dive(n.id)}
        onPaneClick={() => select(null)}>
        <Background color={theme.border} gap={20} />
        <FocusEdge />
        <Controls showInteractive={false} />
      </ReactFlow>
    </Area>
  )
}
