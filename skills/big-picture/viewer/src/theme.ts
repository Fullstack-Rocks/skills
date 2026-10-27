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
  endpoint: theme.lime, function: theme.mint, module: theme.sky, table: theme.violet, database: theme.violet, model: theme.amber, lookup: theme.coral, operation: '#F9A8D4', 'api-model': theme.amber, capsule: '#FDE047', system: theme.sky, topic: '#FB923C', message: '#2DD4BF',
  folder: theme.muted,
}
const EDGE_COLORS: Record<string, string> = {
  calls: '#94A3B8', 'handled-by': theme.lime, reads: theme.sky, writes: theme.violet, 'maps-to': theme.amber, reaches: theme.mint,
  references: theme.violet, 'selects-from': theme.sky, 'looks-up': theme.coral, through: theme.coral, finds: theme.coral,
  'implemented-by': '#F9A8D4', accepts: theme.amber, returns: theme.amber, has: theme.amber, 'calls-api': '#F9A8D4',
  publishes: '#FB923C', consumes: '#FB923C', sends: '#2DD4BF', receives: '#2DD4BF',
}

// Colours the project's view files give its own node types and connection kinds; a value may be a
// CSS gradient (Valkey's blue to purple), whose first colour stands in where one colour is needed.
const custom = new Map<string, string>()

export function setCustomColors(colors: Record<string, string>): void {
  custom.clear()
  for (const [name, value] of Object.entries(colors)) custom.set(name, value)
}

function solid(value: string | undefined): string | undefined {
  return value?.match(/#[0-9a-fA-F]{3,8}/)?.[0]
}

export function typeColor(type: string): string {
  return solid(custom.get(type)) ?? TYPE_COLORS[type] ?? '#9CA3AF'
}

/** The type's full colour: a gradient when its view gives one. */
export function typeFill(type: string): string {
  return custom.get(type) ?? typeColor(type)
}

export function edgeColor(kind: string): string {
  return solid(custom.get(kind)) ?? EDGE_COLORS[kind] ?? '#5B6472'
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
