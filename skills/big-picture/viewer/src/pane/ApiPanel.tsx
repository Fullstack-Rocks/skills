import { useState } from 'react'
import styled from 'styled-components'

import { ends } from '../data/describe'
import { useGraph, type LoadedGraph } from '../store/graph'
import { theme } from '../theme'
import type { GraphNode } from '../types'
import { NodeLink, Section } from './Connections'

// An API operation or endpoint: what the OpenAPI document says it takes and returns, and a Try it
// panel that sends the request (through serve.py's localhost-only proxy when the map is served live).
const Tree = styled.ul`
  margin: 0; padding: 0 0 0 12px; list-style: none; font: 12px ${theme.mono}; border-left: 1px solid ${theme.border};
  li { padding: 2px 0; } b { font-weight: 500; } span { color: ${theme.sky}; } i { color: ${theme.coral}; font-style: normal; }
`
const Field = styled.input`
  width: 100%; padding: 6px 8px; border-radius: 6px; border: 1px solid ${theme.border}; background: ${theme.bg}; font: 12px ${theme.mono};
`
const Body = styled.textarea`
  width: 100%; min-height: 110px; padding: 8px; border-radius: 6px; border: 1px solid ${theme.border}; background: ${theme.bg}; font: 12px ${theme.mono};
`
const Send = styled.button`
  padding: 7px 18px; border: 0; border-radius: 8px; background: ${theme.lime}; color: ${theme.bg}; font-weight: 600; cursor: pointer;
`
const Output = styled.pre`margin: 0; padding: 8px 10px; border-radius: 6px; background: ${theme.bg}; font: 12px ${theme.mono}; white-space: pre-wrap; max-height: 320px; overflow: auto;`
const SAMPLE: Record<string, unknown> = { integer: 0, number: 0, string: '', boolean: false, array: [], object: {} }

function ModelTree({ graph, name, depth = 0 }: { graph: LoadedGraph; name?: string | null; depth?: number }) {
  const model = graph.byId.get(`api-model:${name}`)
  if (!name || !model) return <Tree><li>{name ?? 'no body'}</li></Tree>
  return (
    <Tree>
      {(model.fields ?? []).map((f) => (
        <li key={f.name}>
          <b>{f.name}</b>{f.required ? <i>{'*'}</i> : ''} <span>{f.type}</span>
          {f.ref && depth < 2 && <ModelTree graph={graph} name={f.ref} depth={depth + 1} />}
        </li>
      ))}
    </Tree>
  )
}

function sampleBody(graph: LoadedGraph, name?: string | null): string {
  const fields = graph.byId.get(`api-model:${name}`)?.fields ?? []
  return fields.length ? JSON.stringify(Object.fromEntries(fields.map((f) => [f.name, SAMPLE[f.type] ?? null])), null, 2) : ''
}

async function send(live: boolean, method: string, url: string, body: string): Promise<string> {
  const headers: Record<string, string> = body ? { 'Content-Type': 'application/json' } : {}
  const started = performance.now()
  if (live) {
    const r = await fetch('proxy', { method: 'POST', body: JSON.stringify({ method, url, headers, body }) })
    if (!r.ok) return `${r.status} ${await r.text()}`
    const answer = await r.json()
    return `${answer.status || 'no response'} · ${answer.ms} ms\n\n${answer.body}`
  }
  const r = await fetch(url, { method, headers, body: body || undefined })
  return `${r.status} · ${Math.round(performance.now() - started)} ms\n\n${await r.text()}`
}

function TryIt({ graph, operation, endpoint }: { graph: LoadedGraph; operation?: GraphNode; endpoint?: GraphNode }) {
  const live = useGraph((s) => s.live)
  const [method, path] = (operation?.name ?? endpoint?.name ?? 'GET /').split(' ')
  const [base, setBase] = useState(operation?.servers?.[0] ?? 'http://localhost:8000')
  const [route, setRoute] = useState(path)
  const [body, setBody] = useState(sampleBody(graph, operation?.request))
  const [result, setResult] = useState('')
  const url = (base.endsWith('/') ? base.slice(0, -1) : base) + route
  const go = () => void send(live, method, url, body).then(setResult).catch((e) => setResult(String(e)))
  return (
    <Section>
      <h4>Try it</h4>
      <Field value={base} onChange={(e) => setBase(e.target.value)} aria-label="Base URL" />
      <div style={{ display: 'flex', gap: 8, margin: '8px 0', alignItems: 'center' }}>
        <b style={{ font: `12px ${theme.mono}`, color: theme.lime }}>{method}</b>
        <Field value={route} onChange={(e) => setRoute(e.target.value)} aria-label="Path: replace {parameters}" />
      </div>
      {method !== 'GET' && <Body value={body} onChange={(e) => setBody(e.target.value)} aria-label="JSON body" />}
      <div style={{ margin: '8px 0' }}><Send onClick={go}>Send</Send></div>
      {result && <Output>{result}</Output>}
    </Section>
  )
}

export function ApiPanel({ node }: { node: GraphNode }) {
  const graph = useGraph((s) => s.graph)!
  if (node.type !== 'operation' && node.type !== 'endpoint') return null
  const operation = node.type === 'operation' ? node : graph.byId.get(ends(graph, node.id, 'implemented-by', 'in')[0] ?? '')
  const endpoint = node.type === 'endpoint' ? node : graph.byId.get(ends(graph, node.id, 'implemented-by', 'out')[0] ?? '')
  return (
    <>
      {operation && node !== operation && <Section><h4>OpenAPI operation</h4><NodeLink id={operation.id} /></Section>}
      {endpoint && node !== endpoint && <Section><h4>Implemented by</h4><NodeLink id={endpoint.id} /></Section>}
      {operation?.parameters?.length ? (
        <Section><h4>Parameters</h4><Tree>{operation.parameters.map((p) => <li key={p.name}><b>{p.name}</b>{p.required ? <i>{'*'}</i> : ''} <span>{p.in}</span></li>)}</Tree></Section>
      ) : null}
      {operation?.request && <Section><h4>Request: {operation.request}</h4><ModelTree graph={graph} name={operation.request} /></Section>}
      {Object.entries(operation?.responses ?? {}).map(([code, model]) => (
        <Section key={code}><h4>Response {code}{model ? `: ${model}` : ''}</h4>{model && <ModelTree graph={graph} name={model} />}</Section>
      ))}
      <TryIt key={node.id} graph={graph} operation={operation} endpoint={endpoint} />
    </>
  )
}
