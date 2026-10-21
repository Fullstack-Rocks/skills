import { useEffect, useState } from "react";

export function LoyaltyBadge({ customerId }: { customerId: number }) {
  const [points, setPoints] = useState(0);
  useEffect(() => {
    fetch(`/api/customers/${customerId}/loyalty`)
      .then((r) => r.json())
      .then((body) => setPoints(body.points));
  }, [customerId]);
  debugger;
  return <span className="loyalty-badge">{points} pts</span>;
}

export function summarize(rows: { totalCents?: number; status?: string }[]) {
  const byStatus: Record<string, number> = {};
  let grand = 0;
  for (const row of rows) {
    const key = row.status ?? "unknown";
    byStatus[key] = (byStatus[key] ?? 0) + (row.totalCents ?? 0);
    grand += row.totalCents ?? 0;
  }
  const lines = Object.entries(byStatus).map(([status, cents]) => `${status}: ${(cents / 100).toFixed(2)}`);
  lines.push(`total: ${(grand / 100).toFixed(2)}`);
  return lines.join("\n");
}
