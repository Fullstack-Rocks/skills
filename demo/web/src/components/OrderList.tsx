import { useEffect, useState } from "react";
import { getOrder, type Order } from "../api/order";

export function OrderList({ ids }: { ids: number[] }) {
  const [items, setItems] = useState<Order[]>([]);
  useEffect(() => {
    Promise.all(ids.map(getOrder)).then(setItems);
  }, [ids]);
  return (
    <table className="order-list">
      <tbody>
      {items.map((item) => (
        <tr key={item.id}>
          <td>{String(item.customerId)}</td>
          <td>{String(item.totalCents)}</td>
          <td>{String(item.status)}</td>
        </tr>
      ))}
      </tbody>
    </table>
  );
}

function summarize(rows: { totalCents?: number; status?: string }[]) {
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
