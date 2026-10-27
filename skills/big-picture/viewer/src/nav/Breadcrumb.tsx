import styled from 'styled-components'

import { useGraph } from '../store/graph'
import { ROOT, useView } from '../store/view'
import { theme } from '../theme'

const Crumbs = styled.nav`
  position: absolute; top: 12px; left: 12px; z-index: 5; display: flex; gap: 6px; align-items: center;
  padding: 6px 10px; border-radius: 8px; background: ${theme.panel}; border: 1px solid ${theme.border}; font-size: 13px;
  button { background: none; border: 0; padding: 0; color: ${theme.muted}; cursor: pointer; }
  button:hover { color: ${theme.text}; }
  b { color: ${theme.lime}; font-weight: 500; }
  span { color: ${theme.border}; }
`

export function Breadcrumb() {
  const graph = useGraph((s) => s.graph)
  const { trail, focus, mode, back } = useView()
  const label = (id: string) => (id === ROOT ? 'Project' : graph?.byId.get(id)?.name ?? id)
  return (
    <Crumbs>
      {trail.map((id, i) => (
        <span key={`${id}-${i}`}><button onClick={() => back(i)}>{label(id)}</button> /</span>
      ))}
      <b>{label(focus)}{mode === 'leaves' ? ' · leaves' : ''}</b>
    </Crumbs>
  )
}
