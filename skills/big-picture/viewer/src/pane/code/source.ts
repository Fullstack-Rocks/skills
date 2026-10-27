// Project files read through serve.py (/src/<path>), once per file per build.
const cache = new Map<string, Promise<string>>()

export function readSource(file: string, builtAt: string): Promise<string> {
  const key = `${builtAt}|${file}`
  if (!cache.has(key)) {
    cache.set(key, fetch(`src/${file}`, { cache: 'no-store' }).then((r) => (r.ok ? r.text() : Promise.reject(new Error(`${file}: HTTP ${r.status}`)))))
  }
  return cache.get(key)!
}
