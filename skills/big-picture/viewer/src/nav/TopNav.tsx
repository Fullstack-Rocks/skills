import styled from 'styled-components'

import { useGraph } from '../store/graph'
import { useView, type Tab } from '../store/view'
import { theme } from '../theme'
import { Logo } from './Logo'
import { Search } from './Search'

const Bar = styled.header`
  display: flex; align-items: center; gap: 16px; height: 52px; padding: 0 16px;
  background: ${theme.bg}; border-bottom: 1px solid ${theme.border};
`
const Brand = styled.div`
  display: flex; align-items: center; gap: 12px; white-space: nowrap;
  b { font-size: 16px; font-weight: 700; letter-spacing: -0.02em; }
`
// "big picture": the brand gradient (lime to sky to violet, as in the README banner), set wide.
const Product = styled.span`
  padding-left: 12px; border-left: 1px solid ${theme.border};
  font-size: 13px; font-weight: 800; letter-spacing: 0.22em; text-transform: uppercase;
  background: linear-gradient(90deg, ${theme.lime} 0%, ${theme.mint} 35%, ${theme.sky} 65%, ${theme.violet} 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
`
const Tabs = styled.nav`
  display: flex; gap: 2px; padding: 3px; border-radius: 9px; background: ${theme.panel}; border: 1px solid ${theme.border};
  button { border: 0; border-radius: 7px; padding: 5px 14px; background: none; color: ${theme.muted}; cursor: pointer; font-size: 13px; }
  button[aria-pressed='true'] { background: ${theme.raised}; color: ${theme.lime}; }
`
const TABS: [Tab, string][] = [['map', 'Map'], ['database', 'Database'], ['endpoints', 'Endpoints']]
const Status = styled.div`
  margin-left: auto; display: flex; align-items: center; gap: 8px; color: ${theme.muted}; font-size: 13px;
  i { width: 8px; height: 8px; border-radius: 50%; background: ${theme.mint}; }
`

function age(builtAt: string): string {
  const minutes = Math.round((Date.now() - Date.parse(builtAt)) / 60000)
  if (minutes < 1) return 'just now'
  return minutes < 60 ? `${minutes}m ago` : `${Math.round(minutes / 60)}h ago`
}

export function TopNav() {
  const graph = useGraph((s) => s.graph)
  const live = useGraph((s) => s.live)
  const { tab, setTab } = useView()
  return (
    <Bar>
      <Brand><Logo /><b>fullstack.rocks</b><Product>big picture</Product></Brand>
      <Tabs>
        {[...TABS, ...(graph?.data.views ?? []).map((v): [Tab, string] => [v.id, v.title])].map(([id, label]) => (
          <button key={id} aria-pressed={tab === id} onClick={() => setTab(id)}>{label}</button>
        ))}
      </Tabs>
      <Search />
      {graph && (
        <Status title={`Rebuild: python3 <big-picture>/scripts/build.py ${graph.data.root}`}>
          <i style={{ background: live ? theme.mint : theme.muted }} />
          {graph.data.nodes.length} nodes · built {age(graph.data.builtAt)}{live ? '' : ' · snapshot'}
        </Status>
      )}
    </Bar>
  )
}
