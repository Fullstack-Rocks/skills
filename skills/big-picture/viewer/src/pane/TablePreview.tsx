import styled from 'styled-components'

import { ends } from '../data/describe'
import { useGraph, type LoadedGraph } from '../store/graph'
import { theme } from '../theme'
import type { Column, GraphNode } from '../types'
import { NodeLink, Section } from './Connections'
import { SourceView } from './code/SourceView'

// What a table is (table, view, materialized view, temporary table), where that comes from, its
// columns with keys and constraints, its indexes; a model's fields; a JSON lookup's path.
const Grid = styled.table`
  width: 100%; border-collapse: collapse; font: 12px ${theme.mono};
  th { text-align: left; color: ${theme.muted}; font-weight: 500; padding: 6px 8px; border-bottom: 1px solid ${theme.border}; }
  td { padding: 6px 8px; border-bottom: 1px solid ${theme.border}; vertical-align: top; }
  tr:hover td { background: ${theme.raised}; }
  i { font-style: normal; font-size: 10px; padding: 1px 5px; border-radius: 3px; margin-right: 4px; white-space: nowrap; }
`
const Note = styled.p`margin: 0; color: ${theme.muted}; font-size: 12.5px;`
const Code = styled.code`display: block; padding: 8px 10px; border-radius: 6px; background: ${theme.bg}; font: 12px ${theme.mono}; white-space: pre-wrap;`

function tag(text: string, color: string) {
  return <i style={{ background: `${color}26`, color }}>{text}</i>
}

function Flags({ column }: { column: Column }) {
  return (
    <>
      {column.pk && tag('PK', theme.lime)}
      {column.references && tag(`FK → ${column.references}`, theme.violet)}
      {!column.nullable && !column.pk && tag('NOT NULL', theme.sky)}
      {column.unique && !column.pk && tag('UNIQUE', theme.mint)}
      {column.default && tag(`DEFAULT ${column.default}`, theme.muted)}
      {column.check && tag(`CHECK ${column.check}`, theme.amber)}
    </>
  )
}

function origin(graph: LoadedGraph, node: GraphNode): string {
  if (node.declared) return `Declared in ${node.file}:${node.start}.`
  const model = ends(graph, node.id, 'maps-to', 'in')[0]
  if (!model) return 'Only seen where code accesses it: no DDL or model declares it, so its structure is unknown.'
  return `No DDL declares it: columns come from the model ${graph.byId.get(model)?.name}; keys are inferred by naming (id, <table>_id).`
}

function Columns({ columns }: { columns?: Column[] }) {
  if (!columns?.length) return null
  return (
    <Section>
      <h4>Columns ({columns.length})</h4>
      <Grid>
        <thead><tr><th>name</th><th>type</th><th>keys and constraints</th></tr></thead>
        <tbody>{columns.map((c) => <tr key={c.name}><td>{c.name}</td><td style={{ color: theme.sky }}>{c.type}</td><td><Flags column={c} /></td></tr>)}</tbody>
      </Grid>
    </Section>
  )
}

function Listing({ title, lines }: { title: string; lines: string[] }) {
  if (!lines.length) return null
  return <Section><h4>{title}</h4>{lines.map((line) => <Code key={line}>{line}</Code>)}</Section>
}

/** The model a table's columns come from, and its code when no DDL declares the table. */
function ModelOf({ model, declared }: { model?: GraphNode; declared?: boolean }) {
  if (!model) return null
  return (
    <>
      <Section><h4>Model</h4><NodeLink id={model.id} /></Section>
      {model.file && !declared && <Section><h4>Model source</h4><SourceView node={model} /></Section>}
    </>
  )
}

function indexLines(node: GraphNode): string[] {
  return (node.indexes ?? []).map((i) => `${i.unique ? 'UNIQUE ' : ''}${i.name} (${i.columns.join(', ')})`)
}

function TableStructure({ graph, node }: { graph: LoadedGraph; node: GraphNode }) {
  return (
    <>
      <Section><h4>{node.kind ?? 'table'}</h4><Note>{origin(graph, node)}</Note></Section>
      <Columns columns={node.columns} />
      <Listing title="Constraints" lines={node.constraints ?? []} />
      <Listing title="Indexes" lines={indexLines(node)} />
      <ModelOf model={graph.byId.get(ends(graph, node.id, 'maps-to', 'in')[0] ?? '')} declared={node.declared} />
    </>
  )
}

export function TablePreview({ node }: { node: GraphNode }) {
  const graph = useGraph((s) => s.graph)!
  if (node.type === 'table') return <TableStructure graph={graph} node={node} />
  if (node.type === 'lookup') {
    return (
      <Section>
        <h4>JSON lookup</h4>
        <Note>Finds a row of {node.to_table} by its {node.to_column} column, matched against the path {node.path} inside {node.table}.{node.column}.</Note>
        <Code>{node.expression}</Code>
      </Section>
    )
  }
  if (!node.fields?.length) return null
  return (
    <Section>
      <h4>Fields ({node.fields.length})</h4>
      <Grid><tbody>{node.fields.map((f) => <tr key={f.name}><td>{f.name}</td><td style={{ color: theme.sky }}>{f.type}</td></tr>)}</tbody></Grid>
    </Section>
  )
}
