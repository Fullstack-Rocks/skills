import { useEffect, useState } from "react";
import { getReview, type Review } from "../api/review";

export function ReviewList({ ids }: { ids: number[] }) {
  const [items, setItems] = useState<Review[]>([]);
  useEffect(() => {
    Promise.all(ids.map(getReview)).then(setItems);
  }, [ids]);
  return (
    <table className="review-list">
      <tbody>
      {items.map((item) => (
        <tr key={item.id}>
          <td>{String(item.productId)}</td>
          <td>{String(item.stars)}</td>
          <td>{String(item.body)}</td>
        </tr>
      ))}
      </tbody>
    </table>
  );
}
