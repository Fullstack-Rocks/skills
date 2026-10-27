import paths from './logo-paths.json'

// The fullstack.rocks rock-hand mark (assets/src/logo_paths.json).
export function Logo({ size = 26, color = '#FFFFFF' }: { size?: number; color?: string }) {
  return (
    <svg width={size} height={size} viewBox="-10 -10 520 520" aria-hidden="true">
      {paths.map((d) => <path key={d.slice(0, 24)} d={d} fill={color} />)}
    </svg>
  )
}
