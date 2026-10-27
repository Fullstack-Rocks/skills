import { useEffect, useMemo, useRef, useState } from 'react'
import styled from 'styled-components'

import { containersOf, search } from '../data/walk'
import { useGraph } from '../store/graph'
import { useView } from '../store/view'
import { theme, typeColor } from '../theme'

const RESULTS = 12

const Box = styled.div`position: relative; width: 340px;`
const Input = styled.input`
  width: 100%; height: 32px; padding: 0 44px 0 12px; border-radius: 8px;
  background: ${theme.panel}; border: 1px solid ${theme.border}; outline: none;
  &:focus { border-color: ${theme.lime}; }
`
const Hint = styled.kbd`position: absolute; right: 8px; top: 6px; color: ${theme.muted}; font: 12px ${theme.mono};`
const List = styled.ul`
  position: absolute; top: 36px; left: 0; right: 0; margin: 0; padding: 4px; list-style: none; z-index: 20;
  background: ${theme.raised}; border: 1px solid ${theme.border}; border-radius: 8px; max-height: 420px; overflow: auto;
`
const Item = styled.li<{ $active: boolean }>`
  display: flex; gap: 8px; align-items: baseline; padding: 6px 8px; border-radius: 6px; cursor: pointer;
  background: ${(p) => (p.$active ? theme.border : 'transparent')};
  span { font: 12px ${theme.mono}; }
  small { margin-left: auto; color: ${theme.muted}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
`

export function Search() {
  const graph = useGraph((s) => s.graph)
  const reveal = useView((s) => s.reveal)
  const [text, setText] = useState('')
  const [active, setActive] = useState(0)
  const input = useRef<HTMLInputElement>(null)
  const hits = useMemo(() => (graph && text.trim() ? search(graph, text.trim(), RESULTS) : []), [graph, text])

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') { e.preventDefault(); input.current?.focus() }
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [])

  const open = (id: string) => {
    if (graph) reveal(id, containersOf(graph, id))
    setText('')
    input.current?.blur()
  }
  const onKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'ArrowDown') setActive((a) => Math.min(a + 1, hits.length - 1))
    if (e.key === 'ArrowUp') setActive((a) => Math.max(a - 1, 0))
    if (e.key === 'Enter' && hits[active]) open(hits[active])
    if (e.key === 'Escape') setText('')
  }

  return (
    <Box>
      <Input ref={input} value={text} placeholder="Search nodes" onKeyDown={onKeyDown}
        onChange={(e) => { setText(e.target.value); setActive(0) }} />
      <Hint>⌘K</Hint>
      {hits.length > 0 && (
        <List>
          {hits.map((id, i) => {
            const node = graph!.byId.get(id)!
            return (
              <Item key={id} $active={i === active} onMouseDown={() => open(id)} onMouseEnter={() => setActive(i)}>
                <span style={{ color: typeColor(node.type) }}>{node.type}</span>
                {node.name}
                <small>{node.file}</small>
              </Item>
            )
          })}
        </List>
      )}
    </Box>
  )
}
