import { NodeResizeControl, NodeToolbar, Position, type Node, type NodeProps } from '@xyflow/react'
import { useState } from 'react'
import styled from 'styled-components'

import { healthColor, theme, typeColor } from '../../theme'

// A folder, module or the Database, drawn as a frame around its members. Selected, it shows an icon
// bar; each icon opens its own options (Arrange) or acts at once (Fit, Open). Its right and bottom
// edges resize it, never smaller than its contents.
export type FrameAction = { kind: 'arrange'; columns: number } | { kind: 'reset' } | { kind: 'fit' } | { kind: 'open' }
export type GroupData = {
  label: string; type: string; health: number; selected: boolean
  minWidth?: number; minHeight?: number; act?: (id: string, action: FrameAction) => void
}
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
const Bar = styled.div`
  display: flex; flex-direction: column; gap: 6px; align-items: flex-start;
  > div { display: flex; gap: 2px; padding: 3px; border-radius: 8px; background: ${theme.panel}; border: 1px solid ${theme.border}; box-shadow: 0 4px 16px #00000066; }
  button { display: flex; align-items: center; gap: 6px; border: 0; border-radius: 6px; padding: 5px 8px; background: none; color: ${theme.text}; cursor: pointer; font-size: 12px; }
  button:hover, button[aria-pressed='true'] { background: ${theme.raised}; color: ${theme.lime}; }
  svg { width: 15px; height: 15px; stroke: currentColor; fill: none; stroke-width: 1.6; }
`
const Corner = styled.div`
  width: 12px; height: 12px; border-right: 2px solid ${theme.muted}; border-bottom: 2px solid ${theme.muted};
  position: absolute; right: 4px; bottom: 4px; cursor: nwse-resize;
`
const ARRANGEMENTS: [string, FrameAction][] = [
  ['1 column', { kind: 'arrange', columns: 1 }], ['2', { kind: 'arrange', columns: 2 }], ['3', { kind: 'arrange', columns: 3 }],
  ['4', { kind: 'arrange', columns: 4 }], ['Row', { kind: 'arrange', columns: 999 }], ['Reset', { kind: 'reset' }],
]

function Options({ id, act }: { id: string; act: (id: string, action: FrameAction) => void }) {
  const [open, setOpen] = useState(false)
  return (
    <Bar>
      <div>
        <button title="Arrange what is inside" aria-pressed={open} onClick={() => setOpen(!open)}>
          <svg viewBox="0 0 16 16"><rect x="2" y="2" width="5" height="5" /><rect x="9" y="2" width="5" height="5" /><rect x="2" y="9" width="5" height="5" /><rect x="9" y="9" width="5" height="5" /></svg>
        </button>
        <button title="Fit the frame to its contents" onClick={() => act(id, { kind: 'fit' })}>
          <svg viewBox="0 0 16 16"><path d="M2 6V2h4M14 6V2h-4M2 10v4h4M14 10v4h-4" /></svg>
        </button>
        <button title="Open: show only this" onClick={() => act(id, { kind: 'open' })}>
          <svg viewBox="0 0 16 16"><path d="M6 3H3v10h10v-3M9 2h5v5M14 2 7 9" /></svg>
        </button>
      </div>
      {open && <div>{ARRANGEMENTS.map(([label, action]) => <button key={label} onClick={() => act(id, action)}>{label}</button>)}</div>}
    </Bar>
  )
}

export function GroupCard({ id, data }: NodeProps<GroupNode>) {
  const accent = typeColor(data.type)
  const limits = { minWidth: data.minWidth, minHeight: data.minHeight }
  return (
    <Frame $accent={accent} $selected={data.selected}>
      {data.act && (
        <NodeToolbar isVisible={data.selected} position={Position.Top} align="start">
          <Options id={id} act={data.act} />
        </NodeToolbar>
      )}
      <NodeResizeControl position="right" {...limits} style={{ background: 'transparent', border: 0, width: 8 }} />
      <NodeResizeControl position="bottom" {...limits} style={{ background: 'transparent', border: 0, height: 8 }} />
      <NodeResizeControl position="bottom-right" {...limits} style={{ background: 'transparent', border: 0 }}><Corner /></NodeResizeControl>
      <Label>
        <span style={{ color: accent }}>{data.type}</span>
        {data.label}
        {data.health > 0 && <i style={{ color: healthColor(data.health) }}>{data.health} findings</i>}
      </Label>
    </Frame>
  )
}
