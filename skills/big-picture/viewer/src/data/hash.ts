import { useGraph } from '../store/graph'
import { useView } from '../store/view'
import { containersOf } from './walk'

// The URL hash holds the selected node id (#/n/<id>), so a link opens the map at that node.
const PREFIX = '#/n/'

function openFromHash(): void {
  const graph = useGraph.getState().graph
  const id = decodeURIComponent(location.hash.slice(PREFIX.length))
  if (!graph || !location.hash.startsWith(PREFIX) || !graph.byId.has(id) || id === useView.getState().selected) return
  useView.getState().reveal(id, containersOf(graph, id))
}

/** Keep hash and selection in step; call once after the first graph loads. */
export function syncHash(): void {
  openFromHash()
  window.addEventListener('hashchange', openFromHash)
  useView.subscribe((state, previous) => {
    if (state.selected === previous.selected) return
    history.replaceState(null, '', state.selected ? PREFIX + encodeURIComponent(state.selected) : location.pathname)
  })
}
