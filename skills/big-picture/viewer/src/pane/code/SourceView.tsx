import { useEffect, useRef, useState } from 'react'
import styled from 'styled-components'

import { useGraph } from '../../store/graph'
import { theme } from '../../theme'
import type { GraphNode } from '../../types'
import { languageFor, monaco } from './monaco'
import { readSource } from './source'

// The node's file in a read-only Monaco editor, scrolled to the node's lines and highlighting them.
const Frame = styled.div`
  height: 520px; border-radius: 8px; overflow: hidden; border: 1px solid ${theme.border};
  .bp-range { background: #ECFE8C14; }
  .bp-range-gutter { border-left: 3px solid ${theme.lime}; }
`
const Note = styled.p`color: ${theme.muted}; margin: 0; font-size: 13px;`

function CodeEditor({ file, text, start, end }: { file: string; text: string; start?: number; end?: number }) {
  const host = useRef<HTMLDivElement>(null)
  useEffect(() => {
    const editor = monaco.editor.create(host.current!, {
      value: text, language: languageFor(file), theme: 'big-picture', readOnly: true, automaticLayout: true,
      minimap: { enabled: false }, scrollBeyondLastLine: false, fontSize: 12, lineHeight: 19, renderLineHighlight: 'none',
      fontFamily: theme.mono, stickyScroll: { enabled: false }, padding: { top: 8 },
    })
    if (start) {
      editor.createDecorationsCollection([{
        range: new monaco.Range(start, 1, end ?? start, 1),
        options: { isWholeLine: true, className: 'bp-range', linesDecorationsClassName: 'bp-range-gutter' },
      }])
      editor.revealLineNearTop(start)
    }
    return () => editor.dispose()
  }, [file, text, start, end])
  return <Frame ref={host} />
}

export function SourceView({ node }: { node: GraphNode }) {
  const live = useGraph((s) => s.live)
  const builtAt = useGraph((s) => s.graph?.data.builtAt ?? '')
  const [text, setText] = useState<string | null>(null)

  useEffect(() => {
    setText(null)
    if (!live || !node.file) return
    let current = true
    readSource(node.file, builtAt).then((body) => current && setText(body)).catch(() => current && setText(''))
    return () => { current = false }
  }, [live, node.file, builtAt])

  if (!live) return <Note>Source is shown when the map is opened through serve.py.</Note>
  if (text === null) return <Note>Loading…</Note>
  return <CodeEditor file={node.file!} text={text} start={node.start} end={node.end} />
}
