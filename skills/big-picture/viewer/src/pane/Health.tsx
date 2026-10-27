import { useState } from 'react'
import styled from 'styled-components'

import type { LoadedGraph } from '../store/graph'
import { ROOT } from '../store/view'
import { healthColor, theme } from '../theme'
import type { Finding } from '../types'
import { NodeLink, Section } from './Connections'

// Every finding on a node and inside it, grouped by rule, each with where it is and how to fix it,
// and a brief to hand the lot to an agent (the same list `bp health <node>` prints).
const Rule = styled.li`
  margin-bottom: 10px; padding: 8px 10px; border-radius: 8px; background: ${theme.bg};
  b { font: 12px ${theme.mono}; }
  p { margin: 4px 0 6px; color: ${theme.muted}; font-size: 12.5px; }
`
const Place = styled.div`font-size: 12px; small { display: block; margin-left: 6px; color: ${theme.muted}; font: 11px ${theme.mono}; }`
const Copy = styled.button`
  margin-left: 8px; padding: 2px 8px; border-radius: 6px; border: 1px solid ${theme.border}; background: ${theme.raised};
  color: ${theme.text}; font-size: 11px; cursor: pointer; text-transform: none; letter-spacing: 0;
`

export function findingsInside(graph: LoadedGraph, id: string): Finding[] {
  if (id === ROOT) return graph.data.findings
  const ids = [id]
  for (let i = 0; i < ids.length; i++) ids.push(...(graph.children.get(ids[i]) ?? []))
  return ids.flatMap((n) => graph.findings.get(n) ?? [])
}

function byRule(findings: Finding[]): [string, Finding[]][] {
  const groups = new Map<string, Finding[]>()
  for (const f of findings) groups.set(f.rule, [...(groups.get(f.rule) ?? []), f])
  return [...groups].sort((a, b) => b[1].length - a[1].length)
}

function brief(id: string, findings: Finding[]): string {
  const sections = byRule(findings).map(([rule, group]) => [
    `## ${rule} (${group.length}, ${group[0].source})`, `How: ${group[0].fix ?? ''}`,
    ...group.map((f) => `- ${f.node} at ${f.sites[0][0]}:${f.sites[0][1] ?? ''}: ${f.detail}`),
  ].join('\n'))
  return [`Fix these health findings in ${id} (${findings.length}). Change nothing else.`, ...sections].join('\n\n')
}

export function HealthList({ graph, id }: { graph: LoadedGraph; id: string }) {
  const [copied, setCopied] = useState(false)
  const findings = findingsInside(graph, id)
  if (!findings.length) return null
  const copy = () => void navigator.clipboard.writeText(brief(id, findings)).then(() => setCopied(true))
  return (
    <Section>
      <h4 style={{ color: healthColor(findings.length) }}>
        Health ({findings.length})<Copy onClick={copy}>{copied ? 'Copied' : 'Copy brief for an agent'}</Copy>
      </h4>
      <ul>
        {byRule(findings).map(([rule, group]) => (
          <Rule key={rule}>
            <b>{rule}</b> · {group.length} · {group[0].source}
            <p>{group[0].fix}</p>
            {group.map((f) => (
              <Place key={f.id}>
                <NodeLink id={f.node} hint={`${f.sites[0][0].split('/').pop()}:${f.sites[0][1] ?? ''}`} />
                <small>{f.detail}</small>
              </Place>
            ))}
          </Rule>
        ))}
      </ul>
    </Section>
  )
}
