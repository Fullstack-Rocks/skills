import { applyNodeChanges, type NodeChange } from '@xyflow/react'
import { useCallback, useRef, type Dispatch, type SetStateAction } from 'react'

import { useView } from '../../store/view'
import type { FlowNode } from '../toFlow'
import type { FrameAction } from './GroupCard'
import { arrange, fitToContents, resetFrame, settle } from './settle'

type SetNodes = Dispatch<SetStateAction<FlowNode[]>>

/** One change's movement: a drag's position delta, or a resize's growth; null for anything else. */
function movement(change: NodeChange<FlowNode>, current: FlowNode[]): { id: string; dx: number; dy: number } | null {
  const before = current.find((n) => 'id' in change && n.id === change.id)
  if (!before) return null
  if (change.type === 'position' && change.dragging && change.position) {
    return { id: change.id, dx: change.position.x - before.position.x, dy: change.position.y - before.position.y }
  }
  if (change.type === 'dimensions' && change.resizing && change.dimensions) {
    const width = before.measured?.width ?? before.width ?? 0
    const height = before.measured?.height ?? before.height ?? 0
    return { id: change.id, dx: change.dimensions.width - width, dy: change.dimensions.height - height }
  }
  return null
}

/** Frame behaviour on the canvas: drags and resizes push neighbours and grow frames; a frame's
 *  options arrange, fit, reset or open it. `laidOut` keeps the automatic layout for Reset. */
export function useFrames(setNodes: SetNodes) {
  const laidOut = useRef<FlowNode[]>([])
  const dive = useView((s) => s.dive)

  const onNodesChange = useCallback((changes: NodeChange<FlowNode>[]) => setNodes((current) => {
    const moved = changes.map((c) => movement(c, current)).find(Boolean)
    const next = applyNodeChanges(changes, current)
    return moved ? settle(next, moved.id, moved.dx, moved.dy) : next
  }), [setNodes])

  const act = useCallback((id: string, action: FrameAction) => {
    switch (action.kind) {
      case 'arrange': return setNodes((all) => arrange(all, id, action.columns))
      case 'reset': return setNodes((all) => resetFrame(all, laidOut.current, id))
      case 'fit': return setNodes((all) => fitToContents(all, id))
      case 'open': return dive(id)
    }
  }, [setNodes, dive])

  return { laidOut, onNodesChange, act }
}
