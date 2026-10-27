import type { Node, NodeProps } from '@xyflow/react'
import styled from 'styled-components'

import { healthColor, theme, typeColor } from '../theme'

// A folder, module or the Database, drawn as a frame around its members.
export type GroupData = { label: string; type: string; health: number; selected: boolean }
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

export function GroupCard({ data }: NodeProps<GroupNode>) {
  const accent = typeColor(data.type)
  return (
    <Frame $accent={accent} $selected={data.selected}>
      <Label>
        <span style={{ color: accent }}>{data.type}</span>
        {data.label}
        {data.health > 0 && <i style={{ color: healthColor(data.health) }}>{data.health} findings</i>}
      </Label>
    </Frame>
  )
}
