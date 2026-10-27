import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'

import { App } from './App'
import { syncHash } from './data/hash'
import { loadGraph } from './data/load'

createRoot(document.getElementById('root')!).render(<StrictMode><App /></StrictMode>)
void loadGraph().then(syncHash)
