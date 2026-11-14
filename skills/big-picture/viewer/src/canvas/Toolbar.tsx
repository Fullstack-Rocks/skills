import styled from 'styled-components'

import { useView, type Direction, type EdgeStyle } from '../store/view'
import { theme } from '../theme'

// Connection style and layout direction, top right of the canvas.
const EDGE_STYLES: [EdgeStyle, string][] = [['default', 'Curved'], ['smoothstep', 'Rounded'], ['step', 'Sharp'], ['straight', 'Straight']]
const DIRECTIONS: [Direction, string][] = [['RIGHT', '→'], ['DOWN', '↓'], ['LEFT', '←'], ['UP', '↑']]

const Bar = styled.div`
  position: absolute; top: 12px; right: 12px; z-index: 5; display: flex; gap: 10px;
`
const Segmented = styled.div`
  display: flex; padding: 3px; gap: 2px; border-radius: 8px; background: ${theme.panel}; border: 1px solid ${theme.border};
  button { border: 0; border-radius: 6px; padding: 4px 10px; background: none; color: ${theme.muted}; cursor: pointer; font-size: 12px; }
  button:hover { color: ${theme.text}; }
  button[aria-pressed='true'] { background: ${theme.raised}; color: ${theme.lime}; }
`

export function Toolbar() {
  const { edgeStyle, direction, setEdgeStyle, setDirection } = useView()
  return (
    <Bar>
      <Segmented role="group" aria-label="Connection style">
        {EDGE_STYLES.map(([value, label]) => (
          <button key={value} aria-pressed={edgeStyle === value} onClick={() => setEdgeStyle(value)}>{label}</button>
        ))}
      </Segmented>
      <Segmented role="group" aria-label="Layout direction">
        {DIRECTIONS.map(([value, label]) => (
          <button key={value} aria-pressed={direction === value} onClick={() => setDirection(value)} title={`Lay out ${value.toLowerCase()}`}>{label}</button>
        ))}
      </Segmented>
    </Bar>
  )
}
