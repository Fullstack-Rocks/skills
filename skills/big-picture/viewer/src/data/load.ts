import { useGraph } from '../store/graph'
import type { GraphData } from '../types'

// The graph comes inlined (export.py) or from serve.py, which the page rechecks every 2 seconds
// so a rebuild shows up without a reload.
const POLL_MS = 2000
const SCHEMA_VERSION = 1

function accept(data: GraphData, live: boolean): void {
  if (data.schemaVersion !== SCHEMA_VERSION) {
    useGraph.getState().setError(`graph.json is schema ${data.schemaVersion}; this viewer reads ${SCHEMA_VERSION}. Update big-picture and rebuild.`)
    return
  }
  useGraph.getState().setGraph(data, live)
}

async function fetchGraph(): Promise<string | null> {
  const response = await fetch('graph.json', { cache: 'no-store' })
  if (!response.ok) throw new Error(`graph.json: HTTP ${response.status}`)
  accept(await response.json(), true)
  return response.headers.get('Last-Modified')
}

async function poll(lastModified: string | null): Promise<void> {
  let modified = lastModified
  try {
    const head = await fetch('graph.json', { method: 'HEAD', cache: 'no-store' })
    if (head.ok && head.headers.get('Last-Modified') !== modified) modified = await fetchGraph()
  } catch {
    // serve.py stopped or is restarting: keep the graph on screen and try again
  }
  setTimeout(() => void poll(modified), POLL_MS)
}

export async function loadGraph(): Promise<void> {
  if (window.__BP_GRAPH__) {
    accept(window.__BP_GRAPH__, false)
    return
  }
  try {
    void poll(await fetchGraph())
  } catch (error) {
    useGraph.getState().setError(`No graph: ${String(error)}. Open this page through big-picture's serve.py.`)
  }
}
