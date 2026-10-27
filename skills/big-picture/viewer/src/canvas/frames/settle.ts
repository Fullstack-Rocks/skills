import { NODE_HEIGHT, NODE_WIDTH } from '../../data/layout'
import type { FlowNode } from '../toFlow'

// Dragging keeps the map tidy: a moved card pushes the cards it would overlap on the same level (and
// they push theirs), and every frame grows, in the direction its contents moved, to keep them inside.
// A frame can also re-arrange its own contents as a grid.
const GAP = 16
const PAD = 20
const HEADER = 48 // room for a frame's label

type Box = { x: number; y: number; w: number; h: number }

function box(n: FlowNode): Box {
  // A frame's set size wins over React Flow's last measurement, which lags one render behind a resize.
  return { x: n.position.x, y: n.position.y, w: n.width ?? n.measured?.width ?? NODE_WIDTH, h: n.height ?? n.measured?.height ?? NODE_HEIGHT }
}

function overlaps(a: Box, b: Box): boolean {
  return a.x < b.x + b.w + GAP && b.x < a.x + a.w + GAP && a.y < b.y + b.h + GAP && b.y < a.y + a.h + GAP
}

/** Push siblings out of the moved card's way along its main direction of travel, cascading. */
function pushSiblings(byId: Map<string, FlowNode>, movedId: string, dx: number, dy: number): void {
  const queue = [movedId]
  for (let steps = 0; queue.length && steps < 200; steps++) {
    const mover = byId.get(queue.shift()!)!
    for (const other of [...byId.values()]) {
      if (other.id === mover.id || other.parentId !== mover.parentId || !overlaps(box(mover), box(other))) continue
      const [m, o] = [box(mover), box(other)]
      const horizontal = Math.abs(dx) >= Math.abs(dy)
      const forward = (horizontal ? dx || o.x - m.x : dy || o.y - m.y) >= 0
      const position = horizontal
        ? { x: forward ? m.x + m.w + GAP : m.x - o.w - GAP, y: o.y }
        : { x: o.x, y: forward ? m.y + m.h + GAP : m.y - o.h - GAP }
      byId.set(other.id, { ...other, position } as FlowNode)
      queue.push(other.id)
    }
  }
}

/** Grow each frame around its contents, deepest first; contents past the left or top edge shift the frame. */
function fitFrames(byId: Map<string, FlowNode>, exact?: string): void {
  const depth = (n: FlowNode): number => (n.parentId ? 1 + depth(byId.get(n.parentId)!) : 0)
  const frames = [...byId.values()].filter((n) => n.type === 'group').sort((a, b) => depth(b) - depth(a))
  for (const frame of frames) {
    const inside = [...byId.values()].filter((n) => n.parentId === frame.id)
    if (!inside.length) continue
    const boxes = inside.map(box)
    const shiftX = Math.max(PAD - Math.min(...boxes.map((b) => b.x)), 0)
    const shiftY = Math.max(HEADER - Math.min(...boxes.map((b) => b.y)), 0)
    for (const n of inside) byId.set(n.id, { ...n, position: { x: n.position.x + shiftX, y: n.position.y + shiftY } } as FlowNode)
    const width = Math.max(...boxes.map((b) => b.x + b.w)) + shiftX + PAD
    const height = Math.max(...boxes.map((b) => b.y + b.h)) + shiftY + PAD
    const f = box(frame)
    const size = frame.id === exact ? { width, height } : { width: Math.max(f.w + shiftX, width), height: Math.max(f.h + shiftY, height) }
    byId.set(frame.id, { ...frame, ...size, position: { x: frame.position.x - shiftX, y: frame.position.y - shiftY } } as FlowNode)
  }
}

/** After a card moved by (dx, dy): push what it overlaps, then grow the frames around everything. */
export function settle(nodes: FlowNode[], movedId: string, dx: number, dy: number): FlowNode[] {
  const byId = new Map(nodes.map((n) => [n.id, n]))
  pushSiblings(byId, movedId, dx, dy)
  fitFrames(byId)
  return nodes.map((n) => byId.get(n.id)!)
}

/** Lay out a frame's own contents as a grid of `columns` (in their current reading order), fit the
 *  frame to them, and push the frame's neighbours if it grew. */
export function arrange(nodes: FlowNode[], frameId: string, columns: number): FlowNode[] {
  const byId = new Map(nodes.map((n) => [n.id, n]))
  const inside = nodes.filter((n) => n.parentId === frameId).sort((a, b) => a.position.y - b.position.y || a.position.x - b.position.x)
  const widths = Array.from({ length: columns }, (_, c) => Math.max(0, ...inside.filter((_, i) => i % columns === c).map((n) => box(n).w)))
  const rows = Math.ceil(inside.length / columns)
  const heights = Array.from({ length: rows }, (_, r) => Math.max(0, ...inside.slice(r * columns, r * columns + columns).map((n) => box(n).h)))
  inside.forEach((n, i) => {
    const [row, column] = [Math.floor(i / columns), i % columns]
    const x = PAD + widths.slice(0, column).reduce((sum, w) => sum + w + GAP, 0)
    const y = HEADER + heights.slice(0, row).reduce((sum, h) => sum + h + GAP, 0)
    byId.set(n.id, { ...n, position: { x, y } } as FlowNode)
  })
  fitFrames(byId, frameId)
  pushSiblings(byId, frameId, 1, 1)
  fitFrames(byId)
  return nodes.map((n) => byId.get(n.id)!)
}

/** The smallest a frame may be: its contents' right and bottom edges plus padding. */
export function contentSize(nodes: FlowNode[], frameId: string): { width: number; height: number } {
  const inside = nodes.filter((n) => n.parentId === frameId).map(box)
  return {
    width: Math.max(...inside.map((b) => b.x + b.w), 0) + PAD,
    height: Math.max(...inside.map((b) => b.y + b.h), HEADER) + PAD,
  }
}

/** Shrink (or grow) a frame to exactly fit its contents. */
export function fitToContents(nodes: FlowNode[], frameId: string): FlowNode[] {
  const byId = new Map(nodes.map((n) => [n.id, n]))
  fitFrames(byId, frameId)
  return nodes.map((n) => byId.get(n.id)!)
}

/** Put a frame and everything inside it back where the automatic layout placed them. */
export function resetFrame(nodes: FlowNode[], laidOut: FlowNode[], frameId: string): FlowNode[] {
  const original = new Map(laidOut.map((n) => [n.id, n]))
  const byId = new Map(nodes.map((n) => [n.id, n]))
  const inside = (n: FlowNode): boolean => n.id === frameId || (!!n.parentId && inside(byId.get(n.parentId)!))
  for (const n of nodes.filter(inside)) {
    const first = original.get(n.id)
    if (first) byId.set(n.id, { ...n, position: first.position, width: first.width, height: first.height } as FlowNode)
  }
  pushSiblings(byId, frameId, 1, 1)
  fitFrames(byId)
  return nodes.map((n) => byId.get(n.id)!)
}
