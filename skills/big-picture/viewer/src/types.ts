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
  fields?: { name: string; type: string }[] // a model's fields, from a project property rule
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
}

declare global {
  interface Window {
    __BP_GRAPH__?: GraphData // inlined by export.py; absent when serve.py serves the page
  }
}
