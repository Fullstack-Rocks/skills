import * as monaco from 'monaco-editor/editor/editor.api'
import 'monaco-editor/basic-languages/monaco.contribution'
import EditorWorker from 'monaco-editor/editor/editor.worker?worker&inline'

import { theme } from '../../theme'

// Monaco with its syntax colouring for every language it ships (no language services: the code is
// read-only). The one worker it needs is inlined, so the single-file build stays offline.
self.MonacoEnvironment = { getWorker: () => new EditorWorker() }

monaco.editor.defineTheme('big-picture', {
  base: 'vs-dark',
  inherit: true,
  rules: [],
  colors: {
    'editor.background': theme.bg,
    'editor.lineHighlightBackground': '#ECFE8C10',
    'editorLineNumber.foreground': '#4B5563',
    'editorLineNumber.activeForeground': theme.lime,
  },
})

/** Monaco's language id for a file, from the extensions its languages register; plaintext if none. */
export function languageFor(file: string): string {
  const name = file.toLowerCase()
  const match = monaco.languages.getLanguages().find((l) =>
    l.extensions?.some((ext) => name.endsWith(ext.toLowerCase())) || l.filenames?.some((f) => name.endsWith(`/${f.toLowerCase()}`) || name === f.toLowerCase()))
  return match?.id ?? 'plaintext'
}

export { monaco }
