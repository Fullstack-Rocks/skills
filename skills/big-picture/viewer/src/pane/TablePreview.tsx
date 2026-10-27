import styled from 'styled-components'

import { ends, tableColumns } from '../data/describe'
import { useGraph, type LoadedGraph } from '../store/graph'
import { theme } from '../theme'
import type { GraphNode } from '../types'
import { NodeLink, Section } from './Connections'
import { SourceView } from './SourceView'

// A table's (or model's) columns with their types, the model they come from, and its code.
const Grid = styled.table`
  width: 100%; border-collapse: collapse; font: 12px ${theme.mono};
  th { text-align: left; color: ${theme.muted}; font-weight: 500; padding: 6px 8px; border-bottom: 1px solid ${theme.border}; }
  td { padding: 6px 8px; border-bottom: 1px solid ${theme.border}; }
  td:last-child { color: ${theme.sky}; }
  tr:hover td { background: ${theme.raised}; }
`

type Preview = { columns: { name: string; type: string }[]; linked?: string; modelWithCode?: GraphNode }

/** A table reads its columns from the model mapped to it; a model is its own source of fields. */
function preview(graph: LoadedGraph, node: GraphNode): Preview {
  if (node.type !== 'table') return { columns: node.fields ?? [], linked: ends(graph, node.id, 'maps-to', 'out')[0] }
  const linked = ends(graph, node.id, 'maps-to', 'in')[0]
  const model = graph.byId.get(linked ?? '')
  return { columns: tableColumns(graph, node), linked, modelWithCode: model?.file ? model : undefined }
}

export function TablePreview({ node }: { node: GraphNode }) {
  const graph = useGraph((s) => s.graph)!
  const { columns, linked, modelWithCode } = preview(graph, node)
  if (!columns.length) return null
  const isTable = node.type === 'table'
  return (
    <>
      <Section>
        <h4>{isTable ? 'Columns' : 'Fields'} ({columns.length})</h4>
        <Grid>
          <thead><tr><th>#</th><th>name</th><th>type</th></tr></thead>
          <tbody>{columns.map((c, i) => <tr key={c.name}><td>{i + 1}</td><td>{c.name}</td><td>{c.type}</td></tr>)}</tbody>
        </Grid>
      </Section>
      {linked && <Section><h4>{isTable ? 'Model' : 'Table'}</h4><NodeLink id={linked} /></Section>}
      {modelWithCode && <Section><h4>Model source</h4><SourceView node={modelWithCode} /></Section>}
    </>
  )
}
