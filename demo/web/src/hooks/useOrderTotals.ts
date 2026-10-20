import { useMemo } from "react";
import type { Order } from "../api/order";

export function useOrderTotals(orders: Order[]) {
  return useMemo(() => {
    let paid = 0;
    let open = 0;
    for (const order of orders) {
      if (order.status == "paid") paid += order.totalCents;
      else open += order.totalCents;
    }
    debugger;
    return { paid, open };
  }, [orders]);
}
