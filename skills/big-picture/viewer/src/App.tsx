import { useState } from 'react'
import styled, { ThemeProvider } from 'styled-components'

import { MapCanvas } from './canvas/MapCanvas'
import { FilterPane } from './filters/FilterPane'
import { TopNav } from './nav/TopNav'
import { NodePane } from './pane/NodePane'
import { useGraph } from './store/graph'
import { GlobalStyle, theme } from './theme'

const PANE_KEY = 'big-picture.pane-width'
const FILTERS_KEY = 'big-picture.filters-open'
const FILTERS_WIDTH = 248
const RAIL_WIDTH = 30
const PANE_MIN = 320
const PANE_DEFAULT = 460

const Shell = styled.div`display: grid; grid-template-rows: auto 1fr; height: 100%; overflow: clip;`
const Workspace = styled.div`display: grid; min-height: 0; background: ${theme.bg};`
const Splitter = styled.div`
  cursor: col-resize; background: ${theme.border}; touch-action: none;
  &:hover, &:active { background: ${theme.lime}; }
`
const Message = styled.p`margin: 48px auto; max-width: 560px; color: ${theme.muted};`

function storedWidth(): number {
  try {
    return Number(localStorage.getItem(PANE_KEY)) || PANE_DEFAULT
  } catch {
    return PANE_DEFAULT
  }
}

function storedFiltersOpen(): boolean {
  try {
    return localStorage.getItem(FILTERS_KEY) !== 'false'
  } catch {
    return true
  }
}

/** Drag the splitter to resize the node pane; the width is remembered in this browser. */
function startResize(event: React.PointerEvent, setWidth: (width: number) => void): void {
  const splitter = event.currentTarget as HTMLElement
  splitter.setPointerCapture(event.pointerId)
  const move = (e: PointerEvent) => setWidth(Math.min(Math.max(window.innerWidth - e.clientX, PANE_MIN), window.innerWidth * 0.8))
  const stop = (e: PointerEvent) => {
    splitter.removeEventListener('pointermove', move)
    splitter.removeEventListener('pointerup', stop)
    try { localStorage.setItem(PANE_KEY, String(window.innerWidth - e.clientX)) } catch { /* private window */ }
  }
  splitter.addEventListener('pointermove', move)
  splitter.addEventListener('pointerup', stop)
}

export function App() {
  const graph = useGraph((s) => s.graph)
  const error = useGraph((s) => s.error)
  const [paneWidth, setPaneWidth] = useState(storedWidth)
  const [filtersOpen, setFiltersOpen] = useState(storedFiltersOpen)
  const toggleFilters = () => {
    setFiltersOpen(!filtersOpen)
    try { localStorage.setItem(FILTERS_KEY, String(!filtersOpen)) } catch { /* private window */ }
  }
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <Shell>
        <TopNav />
        {error && <Message>{error}</Message>}
        {!error && !graph && <Message>Loading the graph…</Message>}
        {graph && (
          <Workspace id="workspace" style={{ gridTemplateColumns: `${filtersOpen ? FILTERS_WIDTH : RAIL_WIDTH}px minmax(0, 1fr) 5px ${paneWidth}px` }}>
            <FilterPane open={filtersOpen} onToggle={toggleFilters} />
            <MapCanvas />
            <Splitter onPointerDown={(e) => startResize(e, setPaneWidth)} title="Drag to resize" />
            <NodePane />
          </Workspace>
        )}
      </Shell>
    </ThemeProvider>
  )
}
