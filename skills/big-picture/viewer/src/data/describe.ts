import type { LoadedGraph } from '../store/graph'
import type { GraphNode } from '../types'

// Plain-language summaries built from the graph's own facts, for the cards and the node pane.

const plural = (n: number, word: string) => `${n} ${word}${n === 1 ? '' : 's'}`
const verb = (n: number, base: string) => (n === 1 ? `${base}s` : base) // 1 function reads, 2 functions read
const names = (graph: LoadedGraph, ids: string[]) =>
  ids.slice(0, 3).map((id) => graph.byId.get(id)?.name ?? id).join(', ') + (ids.length > 3 ? ` and ${ids.length - 3} more` : '')

export function ends(graph: LoadedGraph, id: string, kind: string, direction: 'out' | 'in'): string[] {
  const edges = direction === 'out' ? graph.outgoing.get(id) : graph.incoming.get(id)
  return [...new Set((edges ?? []).filter((e) => e.kind === kind).map((e) => (direction === 'out' ? e.to : e.from)))]
}

/** A table's columns: the fields of the model that maps to it. */
export function tableColumns(graph: LoadedGraph, table: GraphNode): { name: string; type: string }[] {
  const model = ends(graph, table.id, 'maps-to', 'in')[0]
  return graph.byId.get(model)?.fields ?? []
}

const descendants = (graph: LoadedGraph, id: string): string[] =>
  (graph.children.get(id) ?? []).flatMap((child) => [child, ...descendants(graph, child)])

/** One short line under a card's name. */
export function subtitle(graph: LoadedGraph, node: GraphNode): string {
  const kids = graph.children.get(node.id) ?? []
  const count = (type: string) => kids.filter((k) => graph.byId.get(k)?.type === type).length
  switch (node.type) {
    case 'function': return `${node.file?.split('/').pop()} · L${node.start}–${node.end} · cx ${node.complexity}`
    case 'endpoint': return `→ ${names(graph, ends(graph, node.id, 'handled-by', 'out'))}`
    case 'table': return `${tableColumns(graph, node).length} columns · read by ${ends(graph, node.id, 'reads', 'in').length} · written by ${ends(graph, node.id, 'writes', 'in').length}`
    case 'model': return `${node.fields?.length ?? 0} fields → ${names(graph, ends(graph, node.id, 'maps-to', 'out')) || 'no table'}`
    case 'module': return [plural(count('function'), 'function'), count('endpoint') ? plural(count('endpoint'), 'endpoint') : ''].filter(Boolean).join(' · ')
    case 'folder': return `${plural(count('module'), 'module')} · ${plural(count('folder'), 'folder')}`
    default: return node.file ?? node.type
  }
}

function describeCode(graph: LoadedGraph, node: GraphNode, entries: string[]): string {
  const calls = ends(graph, node.id, 'calls', 'out')
  const callers = ends(graph, node.id, 'calls', 'in')
  const reads = ends(graph, node.id, 'reads', 'out')
  const writes = ends(graph, node.id, 'writes', 'out')
  return [
    `A function in ${node.file}, lines ${node.start}–${node.end}, cyclomatic complexity ${node.complexity}.`,
    calls.length ? `It calls ${plural(calls.length, 'function')} (${names(graph, calls)}).` : 'It calls no other project function.',
    reads.length || writes.length ? `It reads ${names(graph, reads) || 'no table'} and writes ${names(graph, writes) || 'no table'}.` : '',
    callers.length ? `${plural(callers.length, 'function')} ${verb(callers.length, 'call')} it (${names(graph, callers)}).` : 'Nothing in the project calls it.',
    entries.length ? `It runs for ${plural(entries.length, 'entry point')}: ${names(graph, entries)}.` : '',
  ].filter(Boolean).join(' ')
}

function describeTable(graph: LoadedGraph, node: GraphNode, entries: string[]): string {
  const readers = ends(graph, node.id, 'reads', 'in')
  const writers = ends(graph, node.id, 'writes', 'in')
  const rules = [...new Set((graph.incoming.get(node.id) ?? []).map((e) => e.via))]
  const columns = tableColumns(graph, node)
  const model = ends(graph, node.id, 'maps-to', 'in')
  return [
    `The database table ${node.name}, found where the code accesses it (rules ${rules.join(', ')}).`,
    columns.length ? `Its ${plural(columns.length, 'column')} come from the model ${names(graph, model)}: ${columns.map((c) => c.name).join(', ')}.` : 'No model maps to it, so its columns are unknown.',
    `${plural(readers.length, 'function')} ${verb(readers.length, 'read')} it (${names(graph, readers) || 'none'}) and ${plural(writers.length, 'function')} ${verb(writers.length, 'write')} it (${names(graph, writers) || 'none'}).`,
    entries.length ? `It is reached from ${plural(entries.length, 'entry point')}: ${names(graph, entries)}.` : '',
  ].filter(Boolean).join(' ')
}

function describeContainer(graph: LoadedGraph, node: GraphNode): string {
  const inside = new Set(descendants(graph, node.id))
  const code = [...inside].filter((id) => graph.byId.get(id)?.type === 'function')
  const edges = [...inside].flatMap((id) => (graph.outgoing.get(id) ?? []).filter((e) => e.kind !== 'contains' && !inside.has(e.to)))
  const incoming = [...inside].flatMap((id) => (graph.incoming.get(id) ?? []).filter((e) => e.kind !== 'contains' && !inside.has(e.from)))
  const tables = [...new Set(edges.filter((e) => e.kind === 'reads' || e.kind === 'writes').map((e) => e.to))]
  const findings = graph.health.get(node.id) ?? 0
  return [
    `A ${node.type} at ${node.file} holding ${plural(code.length, 'function')}.`,
    `Code inside makes ${plural(edges.length, 'connection')} out and receives ${plural(incoming.length, 'connection')} from elsewhere.`,
    tables.length ? `It touches the tables ${names(graph, tables)}.` : '',
    `${plural(findings, 'health finding')} inside.`,
  ].filter(Boolean).join(' ')
}

/** A few sentences on what the node is and how it connects; entries from walk.entryPoints. */
export function describe(graph: LoadedGraph, node: GraphNode, entries: string[]): string {
  switch (node.type) {
    case 'function': return describeCode(graph, node, entries)
    case 'endpoint': return `An HTTP endpoint declared in ${node.file}:${node.start}, handled by ${names(graph, ends(graph, node.id, 'handled-by', 'out'))}. Show leaves lists every table and function it ends at.`
    case 'table': return describeTable(graph, node, entries)
    case 'model': return `A data model in ${node.file}, lines ${node.start}–${node.end}, with ${plural(node.fields?.length ?? 0, 'field')}. It maps to the table ${names(graph, ends(graph, node.id, 'maps-to', 'out')) || '(none found)'}.`
    case 'module':
    case 'folder': return describeContainer(graph, node)
    default: return `A ${node.type} file at ${node.file}.`
  }
}
