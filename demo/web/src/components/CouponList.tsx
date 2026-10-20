import { useEffect, useState } from "react";
import { getCoupon, type Coupon } from "../api/coupon";

export function CouponList({ ids }: { ids: number[] }) {
  const [items, setItems] = useState<Coupon[]>([]);
  useEffect(() => {
    Promise.all(ids.map(getCoupon)).then(setItems);
  }, [ids]);
  return (
    <table className="coupon-list">
      <tbody>
      {items.map((item) => (
        <tr key={item.id}>
          <td>{String(item.code)}</td>
          <td>{String(item.percentOff)}</td>
          <td>{String(item.active)}</td>
        </tr>
      ))}
      </tbody>
    </table>
  );
}
