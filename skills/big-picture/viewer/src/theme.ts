import { createGlobalStyle } from 'styled-components'

// fullstack.rocks brand: dark ground, lime accent (assets/src/build_graphics.py uses the same values).
export const theme = {
  bg: '#0B0D10',
  panel: '#12151A',
  raised: '#181C23',
  border: '#232832',
  text: '#E6E8EB',
  muted: '#8B93A1',
  lime: '#ECFE8C',
  sky: '#38BDF8',
  mint: '#7CF5C6',
  violet: '#A78BFA',
  amber: '#FBBF24',
  coral: '#FB7185',
  mono: 'ui-monospace, "SF Mono", Menlo, Consolas, monospace',
  sans: 'Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif',
}

const TYPE_COLORS: Record<string, string> = {
  endpoint: theme.lime, function: theme.mint, module: theme.sky, table: theme.violet, database: theme.violet, model: theme.amber, lookup: theme.coral,
  folder: theme.muted,
}
const EDGE_COLORS: Record<string, string> = {
  calls: '#94A3B8', 'handled-by': theme.lime, reads: theme.sky, writes: theme.violet, 'maps-to': theme.amber, reaches: theme.mint,
  references: theme.violet, 'selects-from': theme.sky, 'looks-up': theme.coral, through: theme.coral, finds: theme.coral,
}

export function typeColor(type: string): string {
  return TYPE_COLORS[type] ?? '#9CA3AF'
}

export function edgeColor(kind: string): string {
  return EDGE_COLORS[kind] ?? '#5B6472'
}

/** Mint when clean, amber for one or two findings, coral from three. */
export function healthColor(findings: number): string {
  if (findings === 0) return theme.mint
  return findings < 3 ? theme.amber : theme.coral
}

export const GlobalStyle = createGlobalStyle`
  *, *::before, *::after { box-sizing: border-box; }
  html, body, #root { height: 100%; margin: 0; }
  body { background: ${theme.bg}; color: ${theme.text}; font: 14px/1.45 ${theme.sans}; -webkit-font-smoothing: antialiased; }
  button, input { font: inherit; color: inherit; }
  a { color: inherit; }
`
