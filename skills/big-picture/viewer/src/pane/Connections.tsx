import { useEffect, useState } from 'react'
import styled from 'styled-components'

import { containersOf, edgesOf } from '../data/walk'
import { useGraph, type LoadedGraph } from '../store/graph'
import { useView } from '../store/view'
import { edgeColor, theme, typeColor } from '../theme'
import type { GraphEdge } from '../types'
import { readSource } from './code/source'

// Edges grouped by kind, outgoing then incoming, named from this node's side (bp node's labels).
const INVERSE: Record<string, string> = {
  calls: 'called by', 'handled-by': 'handles', contains: 'in', reads: 'read by', writes: 'written by',
  'maps-to': 'mapped by', references: 'referenced by', 'selects-from': 'selected by', 'looks-up': 'looked up by',
  through: 'looked up through', finds: 'found by lookup', defines: 'defined in',
}
const GROUP_MAX = 40

export const Section = styled.section`
  h4 { margin: 0 0 6px; font-size: 12px; font-weight: 600; color: ${theme.muted}; text-transform: uppercase; letter-spacing: 0.04em; }
  ul { margin: 0; padding: 0; list-style: none; }
`
export const Link = styled.button`
  display: flex; width: 100%; gap: 8px; align-items: baseline; padding: 4px 6px; border: 0; border-radius: 6px;
  background: none; cursor: pointer; text-align: left;
  &:hover { background: ${theme.raised}; }
  span { font: 11px ${theme.mono}; }
  small { margin-left: auto; color: ${theme.muted}; font: 11px ${theme.mono}; white-space: nowrap; }
`

const Code = styled.code`
  display: block; margin: 0 0 4px 6px; padding: 3px 8px; border-radius: 4px; background: ${theme.bg};
  color: ${theme.muted}; font: 11px ${theme.mono}; white-space: pre; overflow: hidden; text-overflow: ellipsis;
`

type Group = { label: string; kind: string; members: [GraphEdge, string][] }

/** The line of code where an edge happens, read live from the project. */
export function SiteLine({ file, line }: { file: string; line: number }) {
  const live = useGraph((s) => s.live)
  const builtAt = useGraph((s) => s.graph?.data.builtAt ?? '')
  const [text, setText] = useState('')
  useEffect(() => {
    if (!live) return
    let current = true
    readSource(file, builtAt).then((body) => current && setText(body.split('\n')[line - 1]?.trim() ?? '')).catch(() => {})
    return () => { current = false }
  }, [live, file, line, builtAt])
  return text ? <Code title={`${file}:${line}`}>{text}</Code> : null
}

function groups(graph: LoadedGraph, id: string): Group[] {
  const found = new Map<string, Group>()
  for (const direction of ['out', 'in'] as const) {
    for (const [edge, other] of edgesOf(graph, id, direction)) {
      const label = direction === 'out' ? edge.kind : INVERSE[edge.kind] ?? `${edge.kind} (in)`
      const group = found.get(label) ?? { label, kind: edge.kind, members: [] }
      group.members.push([edge, other])
      found.set(label, group)
    }
  }
  return [...found.values()]
}

/** A clickable node id: opens it in the pane and moves the map to its container. */
export function NodeLink({ id, hint }: { id: string; hint?: string }) {
  const graph = useGraph((s) => s.graph)!
  const reveal = useView((s) => s.reveal)
  const node = graph.byId.get(id) ?? { id, type: '?', name: id }
  return (
    <Link onClick={() => reveal(id, containersOf(graph, id))} title={id}>
      <span style={{ color: typeColor(node.type) }}>{node.type}</span>
      {node.name}
      {hint && <small>{hint}</small>}
    </Link>
  )
}

export function Connections({ id }: { id: string }) {
  const graph = useGraph((s) => s.graph)!
  return (
    <>
      {groups(graph, id).map(({ label, kind, members }) => (
        <Section key={label}>
          <h4 style={{ color: edgeColor(kind) }}>{label} ({members.length})</h4>
          <ul>
            {members.slice(0, GROUP_MAX).map(([edge, other]) => (
              <li key={`${label}-${other}`}>
                <NodeLink id={other} hint={`${edge.resolved === 'approx' ? '~ ' : ''}${edge.sites[0] ? `:${edge.sites[0][1]}` : ''}`} />
                {edge.sites[0] && <SiteLine file={edge.sites[0][0]} line={edge.sites[0][1]} />}
              </li>
            ))}
          </ul>
        </Section>
      ))}
    </>
  )
}
