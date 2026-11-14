import { useMemo, useState } from 'react'
import styled from 'styled-components'

import { visibleGraph } from '../data/views'
import { useGraph, type LoadedGraph } from '../store/graph'
import { useView } from '../store/view'
import { edgeColor, theme, typeColor } from '../theme'
import { sectionName, viewContents, type Hidden } from './filterView'

// The left pane: what the canvas holds, by node type, connection kind and section, each with a count;
// clicking one hides it from the canvas (and from every tab) until it is clicked again or Show all.
const SECTIONS_SHOWN = 60

const Pane = styled.aside`
  min-height: 0; min-width: 0; overflow: hidden auto; background: ${theme.panel}; border-right: 1px solid ${theme.border};
  padding: 14px 12px; display: flex; flex-direction: column; gap: 14px; font-size: 13px;
`
const Head = styled.div`
  display: flex; align-items: center; gap: 8px;
  h2 { margin: 0; font-size: 14px; font-weight: 600; flex: 1; }
  button { border: 1px solid ${theme.border}; background: ${theme.raised}; color: ${theme.text}; border-radius: 6px;
    padding: 3px 8px; cursor: pointer; font-size: 12px; }
  button:hover { border-color: ${theme.lime}; }
`
const Find = styled.input`
  width: 100%; box-sizing: border-box; padding: 6px 8px; border-radius: 6px; border: 1px solid ${theme.border};
  background: ${theme.bg}; color: ${theme.text}; font-size: 12px;
`
const Group = styled.section`
  display: flex; flex-direction: column; gap: 2px;
  h3 { margin: 0 0 4px; font-size: 11px; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; color: ${theme.muted}; }
`
const Row = styled.button`
  display: flex; align-items: center; gap: 8px; width: 100%; padding: 4px 6px; border: 0; border-radius: 6px;
  background: none; color: ${theme.text}; cursor: pointer; text-align: left; font-size: 12px;
  &:hover { background: ${theme.raised}; }
  &[aria-pressed='false'] { color: ${theme.muted}; text-decoration: line-through; }
  i { flex: none; width: 10px; height: 10px; border-radius: 3px; border: 1.5px solid; }
  span { flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  small { color: ${theme.muted}; font: 11px ${theme.mono}; text-decoration: none; }
`
const Rail = styled.button`
  border: 0; border-right: 1px solid ${theme.border}; background: ${theme.panel}; color: ${theme.muted}; cursor: pointer;
  writing-mode: vertical-rl; font-size: 12px; letter-spacing: .08em; padding: 12px 0;
  &:hover { color: ${theme.lime}; }
`

type Item = { value: string; label: string; count: number; color: string }

/** One group's rows: what the view holds, plus what is hidden but not in it, so it can be shown again. */
function items(counts: Map<string, number>, hidden: string[], label: (value: string) => string, color: (value: string) => string): Item[] {
  const values = [...new Set([...counts.keys(), ...hidden])]
  return values.map((value) => ({ value, label: label(value), count: counts.get(value) ?? 0, color: color(value) }))
    .sort((a, b) => b.count - a.count || a.label.localeCompare(b.label))
}

function FilterGroup({ title, group, rows, find }: { title: string; group: keyof Hidden; rows: Item[]; find: string }) {
  const { hidden, toggleHidden } = useView()
  const matching = rows.filter((r) => r.label.toLowerCase().includes(find))
  if (!matching.length) return null
  return (
    <Group>
      <h3>{title}</h3>
      {matching.map((r) => {
        const shown = !hidden[group].includes(r.value)
        return (
          <Row key={r.value} aria-pressed={shown} title={`${shown ? 'Hide' : 'Show'} ${r.label}`} onClick={() => toggleHidden(group, r.value)}>
            <i style={{ borderColor: r.color, background: shown ? r.color : 'none' }} /><span>{r.label}</span><small>{r.count}</small>
          </Row>
        )
      })}
    </Group>
  )
}

function useContents(graph: LoadedGraph) {
  const { focus, mode, tab } = useView()
  return useMemo(() => viewContents(graph, visibleGraph(graph, focus, mode, tab)), [graph, focus, mode, tab])
}

function Filters({ graph, onClose }: { graph: LoadedGraph; onClose: () => void }) {
  const { hidden, showAll } = useView()
  const [find, setFind] = useState('')
  const contents = useContents(graph)
  const anyHidden = hidden.types.length + hidden.kinds.length + hidden.sections.length > 0
  const sections = items(contents.sections, hidden.sections, (id) => sectionName(graph, id), (id) => typeColor(graph.byId.get(id)?.type ?? 'folder'))
  return (
    <Pane aria-label="Filters">
      <Head>
        <h2>Filters</h2>
        {anyHidden && <button onClick={showAll}>Show all</button>}
        <button onClick={onClose} title="Collapse the filters">‹</button>
      </Head>
      <Find placeholder="Find a type, connection or section" value={find} onChange={(e) => setFind(e.target.value.toLowerCase())} />
      <FilterGroup title="Nodes" group="types" find={find} rows={items(contents.types, hidden.types, (t) => t, typeColor)} />
      <FilterGroup title="Connections" group="kinds" find={find} rows={items(contents.kinds, hidden.kinds, (k) => k, edgeColor)} />
      <FilterGroup title="Sections" group="sections" find={find} rows={sections.slice(0, find ? undefined : SECTIONS_SHOWN)} />
    </Pane>
  )
}

/** The filter pane, or a slim rail that opens it. */
export function FilterPane({ open, onToggle }: { open: boolean; onToggle: () => void }) {
  const graph = useGraph((s) => s.graph)
  const hiddenCount = useView((s) => s.hidden.types.length + s.hidden.kinds.length + s.hidden.sections.length)
  if (!graph) return null
  if (!open) return <Rail onClick={onToggle} title="Open the filters">Filters{hiddenCount ? ` · ${hiddenCount} hidden` : ''}</Rail>
  return <Filters graph={graph} onClose={onToggle} />
}
