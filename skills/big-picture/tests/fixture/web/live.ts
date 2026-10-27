// Fixture browser client: asks for prices and receives them over the socket.
import { socket, type Handler } from "./socket";

export function watchPrices(sku: string, show: Handler): void {
  socket.on("price.update", show);
  socket.emit("subscribe", { sku });
}
