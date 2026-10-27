import { Background, Controls, ReactFlow, useNodesState, useReactFlow, type Edge } from '@xyflow/react'
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
import { GroupCard } from './frames/GroupCard'
import { Toolbar } from './Toolbar'
import { NodeCard } from './NodeCard'
import { contentSize } from './frames/settle'
import { useFrames } from './frames/useFrames'
import { highlightEdges, toFlowEdges, toFlowNodes, type FlowNode } from './toFlow'

const NODE_TYPES = { card: NodeCard, group: GroupCard }

const Area = styled.main`
  position: relative; min-width: 0; min-height: 0;
  .react-flow { background: ${theme.bg}; }
  .react-flow__node-group { padding: 0; border: 0; background: none; box-shadow: none; }
  .react-flow__controls button { background: ${theme.panel}; border-color: ${theme.border}; fill: ${theme.text}; }
`
const Status = styled.div`position: absolute; inset: 0; display: grid; place-items: center; color: ${theme.muted};`

const minimum = ({ width, height }: { width: number; height: number }) => ({ minWidth: width, minHeight: height })

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
  const { laidOut, onNodesChange, act } = useFrames(setNodes)
  // Cards dim around a focused connection; frames get their options and the smallest size they may take.
  const shown = useMemo(() => nodes.map((n): FlowNode => (n.type === 'card'
    ? (ends ? { ...n, data: { ...n.data, dimmed: n.id !== ends.source && n.id !== ends.target } } : n)
    : { ...n, data: { ...n.data, act, ...minimum(contentSize(nodes, n.id)) } })),
  [nodes, ends, act])
  const [layoutId, setLayoutId] = useState(0) // remounts the flow after each layout so it fits the view

  useEffect(() => {
    if (!graph) return
    let current = true
    const view = visibleGraph(graph, focus, mode, tab)
    void elkLayout(graph, view, direction).then((placed) => {
      if (!current) return
      laidOut.current = toFlowNodes(graph, placed, view, focus, direction)
      setNodes(laidOut.current)
      setEdges(toFlowEdges(view, useView.getState().edgeStyle))
      setLayoutId((n) => n + 1)
    })
    return () => { current = false }
  }, [graph, focus, mode, direction, tab, setNodes, laidOut])

  // Selection only restyles; it keeps positions the person dragged.
  useEffect(() => {
    setNodes((all) => all.map((n) => (n.data.selected === (n.id === selected) ? n : { ...n, data: { ...n.data, selected: n.id === selected } } as FlowNode)))
  }, [selected, layoutId, setNodes])

  return (
    <Area>
      {tab !== 'database' && <Breadcrumb />}
      <Toolbar />
      {layoutId === 0 && <Status>Laying out the graph…</Status>}
      <ReactFlow key={layoutId} nodes={shown} edges={edges} nodeTypes={NODE_TYPES} onNodesChange={onNodesChange}
        onEdgeClick={(_, e) => selectEdge({ id: e.id, source: e.source, target: e.target, label: String(e.label), members: (e.data?.members ?? []) as GraphEdge[] })}
        fitView fitViewOptions={{ maxZoom: 1, padding: 0.08 }} minZoom={0.05} zoomOnDoubleClick={false}
        nodesConnectable={false} proOptions={{ hideAttribution: true }}
        onNodeClick={(_, n) => select(n.id)} onNodeDoubleClick={(_, n) => tab !== 'database' && n.id !== focus && dive(n.id)}
        onPaneClick={() => select(null)}>
        <Background color={theme.border} gap={20} />
        <FocusEdge />
        <Controls showInteractive={false} />
      </ReactFlow>
    </Area>
  )
}
