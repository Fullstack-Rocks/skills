// graph.json, as big-picture's references/graph-schema.md defines it (schema version 1).

export type GraphNode = {
  id: string
  type: string
  name: string
  file?: string
  start?: number
  end?: number
  signature?: string
  complexity?: number
  lines?: number
  fields?: { name: string; type: string; required?: boolean; ref?: string }[] // a model's fields (project rule or OpenAPI)
  // tables: what they are and their structure, from SQL DDL or inferred from a model
  kind?: string
  declared?: boolean
  columns?: Column[]
  constraints?: string[]
  indexes?: { name: string; unique: boolean; columns: string[] }[]
  // JSON lookups
  table?: string
  column?: string
  path?: string
  to_table?: string
  to_column?: string
  expression?: string
  // OpenAPI operations
  method?: string // and `path`, shared with lookups: the operation's URL path
  summary?: string
  operationId?: string
  servers?: string[]
  request?: string | null
  responses?: Record<string, string | null>
  parameters?: { name: string; in: string; required: boolean }[]
  // notes and capsules
  hash?: string
  doc?: string
  docText?: string
  docStale?: boolean
  members?: number
}

export type Column = {
  name: string; type: string; pk: boolean; nullable: boolean; unique: boolean
  references?: string; default?: string; check?: string; inferred?: boolean
}

export type GraphEdge = {
  from: string
  to: string
  kind: string
  via: string
  resolved: 'exact' | 'approx'
  sites: [string, number][]
}

export type Finding = {
  id: string
  rule: string
  node: string
  detail: string
  source: string
  sites: [string, number | null][]
  fix?: string
}

export type GraphData = {
  schemaVersion: number
  builtAt: string
  root: string
  coverage: Record<string, string>
  nodes: GraphNode[]
  edges: GraphEdge[]
  findings: Finding[]
  repeats?: { kind: 'operation' | 'shape'; key: string; sites: [string, number, string][] }[]
  views?: Lens[]
}

// An extra tab defined by a file in .big-picture/views (big-picture's stages/views.py).
export type Lens = { id: string; title: string; types: string[]; edges?: string[] | null; neighbors: boolean; colors: Record<string, string> }

declare global {
  interface Window {
    __BP_GRAPH__?: GraphData // inlined by export.py; absent when serve.py serves the page
  }
}
