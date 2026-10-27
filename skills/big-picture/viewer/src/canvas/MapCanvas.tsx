import { Background, Controls, ReactFlow, useNodesState, type Edge } from '@xyflow/react'
import '@xyflow/react/dist/style.css'
import { useEffect, useMemo, useState } from 'react'
import styled from 'styled-components'

import { elkLayout } from '../data/layout'
import { visibleGraph } from '../data/views'
import { Breadcrumb } from '../nav/Breadcrumb'
import { useGraph } from '../store/graph'
import { useView } from '../store/view'
import { theme } from '../theme'
import { GroupCard } from './GroupCard'
import { Toolbar } from './Toolbar'
import { NodeCard } from './NodeCard'
import { highlightEdges, toFlowEdges, toFlowNodes, type FlowNode } from './toFlow'

const NODE_TYPES = { card: NodeCard, group: GroupCard }

const Area = styled.main`
  position: relative; min-width: 0; min-height: 0;
  .react-flow { background: ${theme.bg}; }
  .react-flow__node-group { padding: 0; border: 0; background: none; box-shadow: none; }
  .react-flow__controls button { background: ${theme.panel}; border-color: ${theme.border}; fill: ${theme.text}; }
`
const Status = styled.div`position: absolute; inset: 0; display: grid; place-items: center; color: ${theme.muted};`

export function MapCanvas() {
  const graph = useGraph((s) => s.graph)
  const { focus, mode, selected, select, dive, direction, edgeStyle } = useView()
  const [nodes, setNodes, onNodesChange] = useNodesState<FlowNode>([])
  const [baseEdges, setEdges] = useState<Edge[]>([])
  const edges = useMemo(() => highlightEdges(baseEdges, nodes, selected).map((e) => ({ ...e, type: edgeStyle })), [baseEdges, nodes, selected, edgeStyle])
  const [layoutId, setLayoutId] = useState(0) // remounts the flow after each layout so it fits the view

  useEffect(() => {
    if (!graph) return
    let current = true
    const view = visibleGraph(graph, focus, mode)
    void elkLayout(graph, view, direction).then((placed) => {
      if (!current) return
      setNodes(toFlowNodes(graph, placed, view, focus, direction))
      setEdges(toFlowEdges(view, useView.getState().edgeStyle))
      setLayoutId((n) => n + 1)
    })
    return () => { current = false }
  }, [graph, focus, mode, direction, setNodes])

  // Selection only restyles; it keeps positions the person dragged.
  useEffect(() => {
    setNodes((all) => all.map((n) => (n.data.selected === (n.id === selected) ? n : { ...n, data: { ...n.data, selected: n.id === selected } } as FlowNode)))
  }, [selected, layoutId, setNodes])

  return (
    <Area>
      <Breadcrumb />
      <Toolbar />
      {layoutId === 0 && <Status>Laying out the graph…</Status>}
      <ReactFlow key={layoutId} nodes={nodes} edges={edges} nodeTypes={NODE_TYPES} onNodesChange={onNodesChange}
        fitView fitViewOptions={{ maxZoom: 1, padding: 0.08 }} minZoom={0.05} zoomOnDoubleClick={false}
        nodesConnectable={false} proOptions={{ hideAttribution: true }}
        onNodeClick={(_, n) => select(n.id)} onNodeDoubleClick={(_, n) => n.id !== focus && dive(n.id)}
        onPaneClick={() => select(null)}>
        <Background color={theme.border} gap={20} />
        <Controls showInteractive={false} />
      </ReactFlow>
    </Area>
  )
}
