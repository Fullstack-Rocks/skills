import type { ClientModule } from 'claude-code'

import type { NavAction, NavChat, NavProps } from '../types'

// The chat sidebar, drawn by a surface module so it can tell a left click from a right one: left
// selects, right opens a menu floating over the list at the click (rename, archive, delete; rename
// for a project). Every list line is one row, so the pointer's row says what was clicked. The last
// column is a handle: dragging it posts the new width, which the pane keeps.

type Menu = { kind: 'chat' | 'project'; target: string; label: string; x: number; y: number }
type Line = { key: string; text: string; action: NavAction; menu?: Omit<Menu, 'x' | 'y'>; chat?: NavChat }
type NavState = { menu?: Menu; mode?: 'menu' | 'rename' | 'delete'; isDragging?: boolean; hover?: number }

const MENU_ROWS = 5 // room kept under the last line so a menu opened there still fits the region
const MIN_WIDTH = 18
const MAX_WIDTH = 60

const Nav: ClientModule<NavProps, NavState> = (props, surface) => {
  const { Box, Text, Button, Input } = surface.elements
  const state = surface.state ?? {}
  const close = () => surface.setState({})
  const lines: Line[] = []
  const none: NavAction = { type: 'none' }
  const blank = (key: string) => lines.push({ key, text: ' ', action: none })

  for (const group of props.groups) {
    const name = group.project || 'No project'
    lines.push({
      key: `p-${group.project}`,
      text: name,
      action: none,
      menu: group.project ? { kind: 'project', target: group.project, label: name } : undefined,
    })
    for (const chat of group.chats) {
      blank(`b-${chat.id}`)
      lines.push({
        key: `c-${chat.id}`,
        text: chat.name,
        action: { type: 'select', target: chat.id },
        menu: { kind: 'chat', target: chat.id, label: chat.name },
        chat,
      })
    }
    blank(`g-${group.project}`)
  }
  lines.push({ key: 'archived', text: `Archived (${props.archived})`, action: { type: 'select', target: '__archived' } })

  // Hover is drawn here from pointer moves: the row under the pointer gets the light background.
  const lit = (i: number, line: Line) =>
    state.hover === i && !state.menu && (line.action.type !== 'none' || line.menu) ? props.hoverColor : undefined

  const row = (line: Line, i: number) => {
    if (line.chat) {
      const isOn = line.chat.id === props.selected
      return (
        <Box key={line.key} flexDirection="row" backgroundColor={lit(i, line)}>
          <Text color={line.chat.color} bold>{`  ${line.chat.glyph} `}</Text>
          <Text bold={isOn} inverse={isOn} wrap="truncate-end">{`${line.chat.name}${line.chat.running ? ' …' : ''}`}</Text>
          {line.chat.unread ? <Text color="#3FB950"> ●</Text> : null}
        </Box>
      )
    }
    const isArchive = line.key === 'archived' && props.selected === '__archived'
    return (
      <Box key={line.key} backgroundColor={lit(i, line)}>
        <Text bold={line.key.startsWith('p-') || isArchive} inverse={isArchive} wrap="truncate-end">
          {line.text}
        </Text>
      </Box>
    )
  }

  // Where the menu floats: under the clicked row, kept inside the region.
  const menuBox = (menu: Menu) => {
    const room = Math.max(24, surface.columns || 30)
    const width = state.mode === 'menu' || !state.mode ? 16 : Math.min(room, 34)
    return { top: menu.y + 1, left: Math.max(0, Math.min(menu.x, room - width)), width, height: 7 }
  }

  // The menu floats at the click, over the list, so nothing under it moves.
  const floating = () => {
    const menu = state.menu
    if (!menu) return null
    const box = menuBox(menu)
    const post = (action: NavAction) => (close(), surface.post(action))
    let body
    if (state.mode === 'rename') {
      body = (
        <Input
          key={`rename-${menu.kind}-${menu.target}`}
          label="Rename"
          value={menu.label}
          autoFocus
          onSubmit={value => {
            const name = value.trim()
            if (!name || name === menu.label) return close()
            post({ type: menu.kind === 'chat' ? 'rename' : 'rename-project', target: menu.target, value: name })
          }}
        />
      )
    } else if (state.mode === 'delete') {
      body = (
        <Box flexDirection="column">
          <Text color="red" wrap="wrap">Delete "{menu.label}", its worktree and transcript?</Text>
          <Box flexDirection="row" gap={1}>
            <Button key="delete-yes" label="Delete" onPress={() => post({ type: 'delete', target: menu.target })} />
            <Button key="delete-no" label="Cancel" plain dimColor onPress={close} />
          </Box>
        </Box>
      )
    } else {
      // Each item is its own keyed Box, so the surface lights the one under the pointer.
      let index = 0
      const item = (key: string, label: string, onPress: () => void, isDim = false) => {
        // The menu's rows start one below its top border.
        const isLit = state.hover === box.top + 1 + index++
        return (
          <Box key={`item-${key}`} backgroundColor={isLit ? props.hoverColor : undefined}>
            <Button key={`menu-${key}`} label={label} plain dimColor={isDim} onPress={onPress} />
          </Box>
        )
      }
      body = (
        <Box flexDirection="column">
          {item('rename', '✎  Rename', () => surface.setState({ menu, mode: 'rename' }))}
          {menu.kind === 'chat' ? item('archive', '⊟  Archive', () => post({ type: 'archive', target: menu.target })) : null}
          {menu.kind === 'chat' ? item('delete', '✕  Delete', () => surface.setState({ menu, mode: 'delete' })) : null}
          {item('cancel', '↩  Cancel', close, true)}
        </Box>
      )
    }
    return (
      <Box
        key="menu"
        position="absolute"
        top={box.top}
        left={box.left}
        width={box.width}
        borderStyle="round"
        borderColor="gray"
        backgroundColor="inverseText"
        paddingX={1}
        flexDirection="column"
      >
        {body}
      </Box>
    )
  }

  // The handle is the region's last column: press, drag, release.
  const handle = Math.max(1, (surface.columns || props.width) - 1)
  surface.onPointer(event => {
    if (state.isDragging) {
      if (event.type === 'move') surface.post({ type: 'resize', width: Math.min(MAX_WIDTH, Math.max(MIN_WIDTH, event.x + 1)) })
      if (event.type === 'up') surface.setState({})
      return
    }
    if (event.type === 'down' && event.button === 'left' && event.x >= handle) {
      surface.setState({ isDragging: true })
      return
    }
    if (event.type === 'leave') {
      if (state.hover !== undefined) surface.setState({ ...state, hover: undefined })
      return
    }
    if (event.type === 'move' && !event.button) {
      const hover = event.x >= handle ? -1 : event.y
      if (hover !== state.hover) surface.setState({ ...state, hover })
      return
    }
    if (event.type !== 'down') return
    const line = lines[event.y]
    if (state.menu) {
      // A click inside the menu belongs to its buttons and field.
      const box = menuBox(state.menu)
      const isInside = event.x >= box.left && event.x < box.left + box.width && event.y >= box.top && event.y < box.top + box.height
      if (isInside) return
      close()
      if (event.button !== 'right') return // a click outside the menu only closes it
    }
    if (!line) return
    if (event.button === 'right') {
      if (line.menu) surface.setState({ menu: { ...line.menu, x: event.x, y: event.y }, mode: 'menu' })
      return
    }
    if (line.action.type !== 'none') surface.post(line.action)
  })

  const height = lines.length + (state.menu ? MENU_ROWS : 0)
  return (
    <Box position="relative" flexDirection="row">
      <Box flexDirection="column" flexGrow={1} flexShrink={1}>
        {lines.map((line, i) => row(line, i))}
        {state.menu ? Array.from({ length: MENU_ROWS }, (_, i) => <Box key={`pad-${i}`}><Text> </Text></Box>) : null}
      </Box>
      <Box key="handle" flexDirection="column" width={1} backgroundColor={state.hover === -1 ? props.hoverColor : undefined}>
        <Text dimColor={!state.isDragging}>{Array.from({ length: height }, () => '│').join('\n')}</Text>
      </Box>
      {floating()}
    </Box>
  )
}

export default Nav
