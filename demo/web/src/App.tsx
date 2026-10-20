import { OrderList } from "./components/OrderList";
import { InvoiceList } from "./components/InvoiceList";

export function App() {
  return (
    <main>
      <OrderList ids={[1, 2, 3]} />
      <InvoiceList ids={[10, 11]} />
    </main>
  );
}
