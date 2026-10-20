import { useEffect, useState } from "react";
import { getWarehouse, type Warehouse } from "../api/warehouse";

export function WarehouseList({ ids }: { ids: number[] }) {
  const [items, setItems] = useState<Warehouse[]>([]);
  useEffect(() => {
    Promise.all(ids.map(getWarehouse)).then(setItems);
  }, [ids]);
  return (
    <table className="warehouse-list">
      <tbody>
      {items.map((item) => (
        <tr key={item.id}>
          <td>{String(item.city)}</td>
          <td>{String(item.capacity)}</td>
          <td>{String(item.open)}</td>
        </tr>
      ))}
      </tbody>
    </table>
  );
}
