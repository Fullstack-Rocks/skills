import { useEffect, useState } from 'react'
import Markdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import styled from 'styled-components'

import { useGraph } from '../../store/graph'
import { theme } from '../../theme'
import type { GraphNode } from '../../types'

// The note an agent wrote about a node (.big-picture/docs/<slug>.md). Served live, the pane rereads
// it every few seconds, so a note appears while the agent is writing it, before any rebuild.
const RECHECK_MS = 3000
const FRONT_MATTER = /^---\n[\s\S]*?\n---\n?/

const Body = styled.div`
  font-size: 13.5px; line-height: 1.6;
  p, ul, ol, pre { margin: 0 0 8px; }
  code { font: 12px ${theme.mono}; background: ${theme.bg}; padding: 1px 4px; border-radius: 4px; }
  pre { padding: 8px 10px; background: ${theme.bg}; border-radius: 6px; overflow: auto; }
  pre code { padding: 0; }
  a { color: ${theme.sky}; }
`
const Stale = styled.span`margin-left: 8px; padding: 1px 6px; border-radius: 4px; background: ${theme.amber}26; color: ${theme.amber}; font-size: 11px;`
const Hint = styled.p`margin: 0; color: ${theme.muted}; font-size: 12.5px; code { font: 11.5px ${theme.mono}; }`

export function noteSlug(id: string): string {
  return id.replace(/[^A-Za-z0-9._-]+/g, '_')
}

export function Note({ node }: { node: GraphNode }) {
  const live = useGraph((s) => s.live)
  const [text, setText] = useState(node.docText ?? '')
  useEffect(() => {
    setText(node.docText ?? '')
    if (!live) return
    const read = () => fetch(`src/.big-picture/docs/${noteSlug(node.id)}.md`, { cache: 'no-store' })
      .then((r) => (r.ok ? r.text() : '')).then((body) => body && setText(body.replace(FRONT_MATTER, ''))).catch(() => {})
    void read()
    const timer = setInterval(read, RECHECK_MS)
    return () => clearInterval(timer)
  }, [live, node.id, node.docText])
  if (!text) return <Hint>No note yet. An agent can write one at <code>.big-picture/docs/{noteSlug(node.id)}.md</code>.</Hint>
  return (
    <section>
      <h4 style={{ margin: '0 0 6px', fontSize: 12, color: theme.muted, textTransform: 'uppercase', letterSpacing: '0.04em' }}>
        Note{node.docStale && <Stale title="The code changed since this note was written">stale</Stale>}
      </h4>
      <Body><Markdown remarkPlugins={[remarkGfm]}>{text}</Markdown></Body>
    </section>
  )
}
