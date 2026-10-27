import { Handle, Position, type Node, type NodeProps } from '@xyflow/react'
import styled from 'styled-components'

import { NODE_HEIGHT, NODE_WIDTH } from '../data/layout'
import type { Direction } from '../store/view'
import { edgeColor, healthColor, theme, typeColor } from '../theme'
import type { GraphNode } from '../types'

// A node: type, name, a detail line and its health dot. Each kind of connection gets its own
// coloured dot on the input side and on the output side, in the colour of its lines.
export type CardData = {
  node: GraphNode; subtitle: string; health: number; focused: boolean; selected: boolean; outside: boolean
  inKinds: string[]; outKinds: string[]; direction: Direction
}
export type CardNode = Node<CardData, 'card'>

const SIDES: Record<Direction, [Position, Position]> = {
  RIGHT: [Position.Left, Position.Right], LEFT: [Position.Right, Position.Left],
  DOWN: [Position.Top, Position.Bottom], UP: [Position.Bottom, Position.Top],
}

const Card = styled.div<{ $accent: string; $selected: boolean; $focused: boolean; $outside: boolean }>`
  width: ${NODE_WIDTH}px; height: ${NODE_HEIGHT}px; padding: 9px 14px; border-radius: 10px; cursor: grab;
  background: ${(p) => (p.$focused ? theme.raised : theme.panel)};
  border: 1px ${(p) => (p.$outside ? 'dashed' : 'solid')} ${(p) => (p.$selected ? p.$accent : theme.border)};
  box-shadow: ${(p) => (p.$selected ? `0 0 0 3px ${p.$accent}33` : '0 1px 0 #00000040')};
  opacity: ${(p) => (p.$outside ? 0.75 : 1)};
  display: grid; grid-template-columns: 1fr auto; grid-template-rows: auto auto auto; column-gap: 8px;
  .react-flow__handle { width: 9px; height: 9px; border: 2px solid ${theme.bg}; min-width: 0; min-height: 0; }
`
const Type = styled.div`font: 10.5px ${theme.mono}; letter-spacing: 0.04em; text-transform: uppercase;`
const Name = styled.div`
  grid-column: 1 / -1; font-size: 14px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
`
const Sub = styled.div`
  grid-column: 1 / -1; color: ${theme.muted}; font: 11px ${theme.mono}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
`
const Dot = styled.i`
  justify-self: end; align-self: center; display: flex; gap: 5px; align-items: center; font: 11px ${theme.mono}; font-style: normal;
  &::after { content: ''; width: 9px; height: 9px; border-radius: 50%; background: currentColor; }
`

function Handles({ kinds, type, position }: { kinds: string[]; type: 'source' | 'target'; position: Position }) {
  const across = position === Position.Left || position === Position.Right ? 'top' : 'left'
  return kinds.map((kind, i) => (
    <Handle key={kind} id={`${type === 'source' ? 'out' : 'in'}-${kind}`} type={type} position={position} title={kind}
      style={{ background: edgeColor(kind), [across]: `${((i + 1) / (kinds.length + 1)) * 100}%` }} />
  ))
}

export function NodeCard({ data }: NodeProps<CardNode>) {
  const { node, subtitle, health, focused, selected, outside, inKinds, outKinds, direction } = data
  const accent = typeColor(node.type)
  const [inSide, outSide] = SIDES[direction]
  return (
    <Card $accent={accent} $selected={selected} $focused={focused} $outside={outside} title={node.id}>
      <Handles kinds={inKinds} type="target" position={inSide} />
      <Type style={{ color: accent }}>{node.type}{outside ? ' · outside' : ''}</Type>
      <Dot style={{ color: healthColor(health) }} title={`${health} health findings`}>{health || ''}</Dot>
      <Name>{node.name.split('/').pop()}</Name>
      <Sub>{subtitle}</Sub>
      <Handles kinds={outKinds} type="source" position={outSide} />
    </Card>
  )
}
