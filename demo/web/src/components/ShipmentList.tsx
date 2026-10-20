import { useEffect, useState } from "react";
import { getShipment, type Shipment } from "../api/shipment";

export function ShipmentList({ ids }: { ids: number[] }) {
  const [items, setItems] = useState<Shipment[]>([]);
  useEffect(() => {
    Promise.all(ids.map(getShipment)).then(setItems);
  }, [ids]);
  return (
    <table className="shipment-list">
      <tbody>
      {items.map((item) => (
        <tr key={item.id}>
          <td>{String(item.orderId)}</td>
          <td>{String(item.carrier)}</td>
          <td>{String(item.tracking)}</td>
        </tr>
      ))}
      </tbody>
    </table>
  );
}
