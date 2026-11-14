import styled from 'styled-components'

import { useView, type SelectedEdge } from '../store/view'
import { edgeColor, theme } from '../theme'
import { NodeLink, Section, SiteLine } from './Connections'

// A clicked connection: what it is, its two ends, and every place in the code it happens.
const Title = styled.h2`margin: 0; font-size: 18px; font-weight: 600;`
const Ends = styled.div`display: grid; grid-template-columns: 1fr auto 1fr; gap: 8px; align-items: center; color: ${theme.muted};`
const Member = styled.li`margin-bottom: 8px;`

export function EdgePane({ edge }: { edge: SelectedEdge }) {
  const select = useView((s) => s.select)
  const kind = edge.members[0]?.kind ?? edge.label
  return (
    <>
      <header>
        <Title style={{ color: edgeColor(kind) }}>{edge.label}</Title>
        <small style={{ color: theme.muted }}>{edge.members.length} connection{edge.members.length === 1 ? '' : 's'} between these two</small>
      </header>
      <Ends><NodeLink id={edge.source} /><span>→</span><NodeLink id={edge.target} /></Ends>
      <Section>
        <h4>Where it happens</h4>
        <ul>
          {edge.members.map((m) => (
            <Member key={`${m.from}|${m.kind}|${m.to}`}>
              <NodeLink id={m.from} hint={`${m.kind}${m.resolved === 'approx' ? ' ~' : ''} → ${m.to.split(/[#:]/).pop()}`} />
              {m.sites.slice(0, 3).map(([file, line]) => <SiteLine key={`${file}:${line}`} file={file} line={line} />)}
            </Member>
          ))}
        </ul>
      </Section>
      <button onClick={() => select(null)} style={{ alignSelf: 'start', background: 'none', border: 0, color: theme.muted, cursor: 'pointer' }}>
        Clear
      </button>
    </>
  )
}
