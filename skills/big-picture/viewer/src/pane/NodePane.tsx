import styled from 'styled-components'

import { describe } from '../data/describe'
import { entryPoints } from '../data/walk'
import { useGraph } from '../store/graph'
import { useView } from '../store/view'
import { theme, typeColor } from '../theme'
import { Connections, NodeLink, Section } from './Connections'
import { SourceView } from './code/SourceView'
import { ApiPanel } from './ApiPanel'
import { EdgePane } from './EdgePane'
import { HealthList } from './Health'
import { TablePreview } from './TablePreview'
import type { GraphNode } from '../types'

const Pane = styled.aside`
  min-height: 0; min-width: 0; overflow: auto; background: ${theme.panel};
  padding: 18px; display: flex; flex-direction: column; gap: 18px;
`
const Title = styled.h2`margin: 0; font-size: 19px; font-weight: 600; word-break: break-word;`
const Badge = styled.span`
  display: inline-block; margin-top: 6px; padding: 1px 8px; border-radius: 999px; font: 11px ${theme.mono};
  border: 1px solid currentColor;
`
const Meta = styled.div`color: ${theme.muted}; font: 12px ${theme.mono}; word-break: break-all;`
const Actions = styled.div`
  display: grid; grid-template-columns: 1fr 1fr; gap: 8px;
  button, a { height: 34px; border-radius: 8px; border: 1px solid ${theme.border}; background: ${theme.raised};
    cursor: pointer; display: flex; align-items: center; justify-content: center; text-decoration: none; font-size: 13px; }
  button:hover, a:hover { border-color: ${theme.lime}; }
`
const Empty = styled.p`color: ${theme.muted}; margin: 0;`
const About = styled.p`margin: 0; line-height: 1.6; color: ${theme.text};`

function fullscreen(): void {
  void document.getElementById('workspace')?.requestFullscreen()
}

function NodeHeader({ node, root }: { node: GraphNode; root: string }) {
  const dive = useView((s) => s.dive)
  const editor = node.file ? `vscode://file${root}/${node.file}${node.start ? `:${node.start}` : ''}` : null
  return (
    <>
      <header>
        <Title>{node.name}</Title>
        <Badge style={{ color: typeColor(node.type) }}>{node.type}</Badge>
        <Meta>{node.file}{node.start ? `:${node.start}-${node.end}` : ''}</Meta>
        {node.signature && <Meta>{node.signature}</Meta>}
      </header>
      <Actions>
        <button onClick={() => dive(node.id)}>Open subgraph</button>
        <button onClick={() => { dive(node.id); fullscreen() }}>Fullscreen</button>
        <button onClick={() => dive(node.id, 'leaves')}>Show leaves</button>
        {editor ? <a href={editor}>Open in editor</a> : <span />}
      </Actions>
    </>
  )
}

function EntryList({ ids }: { ids: string[] }) {
  if (!ids.length) return null
  return <Section><h4>Entry points ({ids.length})</h4><ul>{ids.map((id) => <li key={id}><NodeLink id={id} /></li>)}</ul></Section>
}

export function NodePane() {
  const graph = useGraph((s) => s.graph)
  const selected = useView((s) => s.selected)
  const selectedEdge = useView((s) => s.selectedEdge)
  const node = selected ? graph?.byId.get(selected) : undefined
  if (graph && selectedEdge) return <Pane><EdgePane edge={selectedEdge} /></Pane>
  if (!graph || !node) {
    return <Pane><Empty>Click a node to see what it is, what it touches and its code. Double-click to dive in.</Empty></Pane>
  }
  const entries = entryPoints(graph, node.id)
  return (
    <Pane>
      <NodeHeader node={node} root={graph.data.root} />
      <About>{describe(graph, node, entries)}</About>
      <TablePreview node={node} />
      <ApiPanel node={node} />
      <EntryList ids={entries} />
      <HealthList graph={graph} id={node.id} />
      <Connections id={node.id} />
      {node.file && node.type !== 'folder' && <Section><h4>Source</h4><SourceView node={node} /></Section>}
    </Pane>
  )
}
