import { useEffect, useState } from "react";
import { getCustomer, type Customer } from "../api/customer";

export function CustomerList({ ids }: { ids: number[] }) {
  const [items, setItems] = useState<Customer[]>([]);
  useEffect(() => {
    Promise.all(ids.map(getCustomer)).then(setItems);
  }, [ids]);
  return (
    <table className="customer-list">
      <tbody>
      {items.map((item) => (
        <tr key={item.id}>
          <td>{String(item.email)}</td>
          <td>{String(item.name)}</td>
          <td>{String(item.tier)}</td>
        </tr>
      ))}
      </tbody>
    </table>
  );
}
