import { NodeToolbar, Position, type Node, type NodeProps } from '@xyflow/react'
import styled from 'styled-components'

import { healthColor, theme, typeColor } from '../theme'

// A folder, module or the Database, drawn as a frame around its members. Selected, it shows an options
// bar that re-arranges what is inside it.
export type GroupData = { label: string; type: string; health: number; selected: boolean; onArrange?: (id: string, columns: number) => void }
export type GroupNode = Node<GroupData, 'group'>

const Frame = styled.div<{ $accent: string; $selected: boolean }>`
  width: 100%; height: 100%; border-radius: 14px; cursor: grab;
  background: ${(p) => p.$accent}0d; border: 1px solid ${(p) => (p.$selected ? p.$accent : `${p.$accent}40`)};
`
const Label = styled.div`
  display: flex; gap: 8px; align-items: baseline; padding: 10px 14px; font-size: 13px; font-weight: 600;
  span { font: 10.5px ${theme.mono}; text-transform: uppercase; letter-spacing: 0.04em; }
  i { margin-left: auto; font: 11px ${theme.mono}; font-style: normal; }
`

const Options = styled.div`
  display: flex; gap: 2px; align-items: center; padding: 3px; border-radius: 8px; background: ${theme.panel};
  border: 1px solid ${theme.border}; box-shadow: 0 4px 16px #00000066; font-size: 12px;
  span { color: ${theme.muted}; padding: 0 6px; }
  button { border: 0; border-radius: 6px; padding: 3px 9px; background: none; color: ${theme.text}; cursor: pointer; }
  button:hover { background: ${theme.raised}; color: ${theme.lime}; }
`
const ARRANGEMENTS: [string, number][] = [['1 column', 1], ['2', 2], ['3', 3], ['4', 4], ['Row', 999]]

export function GroupCard({ id, data }: NodeProps<GroupNode>) {
  const accent = typeColor(data.type)
  return (
    <Frame $accent={accent} $selected={data.selected}>
      <NodeToolbar isVisible={data.selected && Boolean(data.onArrange)} position={Position.Top} align="start">
        <Options>
          <span>Arrange</span>
          {ARRANGEMENTS.map(([label, columns]) => (
            <button key={label} onClick={() => data.onArrange?.(id, columns)} title={columns === 999 ? 'All in one row' : `Grid of ${columns}`}>{label}</button>
          ))}
        </Options>
      </NodeToolbar>
      <Label>
        <span style={{ color: accent }}>{data.type}</span>
        {data.label}
        {data.health > 0 && <i style={{ color: healthColor(data.health) }}>{data.health} findings</i>}
      </Label>
    </Frame>
  )
}
