import { useEffect, useState } from "react";
import { getInvoice, type Invoice } from "../api/invoice";

export function InvoiceList({ ids }: { ids: number[] }) {
  const [items, setItems] = useState<Invoice[]>([]);
  useEffect(() => {
    Promise.all(ids.map(getInvoice)).then(setItems);
  }, [ids]);
  return (
    <table className="invoice-list">
      <tbody>
      {items.map((item) => (
        <tr key={item.id}>
          <td>{String(item.orderId)}</td>
          <td>{String(item.dueDays)}</td>
          <td>{String(item.paid)}</td>
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
