import { useEffect, useState } from "react";
import { getProduct, type Product } from "../api/product";

export function ProductList({ ids }: { ids: number[] }) {
  const [items, setItems] = useState<Product[]>([]);
  useEffect(() => {
    Promise.all(ids.map(getProduct)).then(setItems);
  }, [ids]);
  return (
    <table className="product-list">
      <tbody>
      {items.map((item) => (
        <tr key={item.id}>
          <td>{String(item.sku)}</td>
          <td>{String(item.priceCents)}</td>
          <td>{String(item.stock)}</td>
        </tr>
      ))}
      </tbody>
    </table>
  );
}
