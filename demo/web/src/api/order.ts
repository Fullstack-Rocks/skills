import { apiClient } from "../lib/apiClient";

export interface Order {
  id: number;
  customerId: number;
  totalCents: number;
  status: string;
}

export async function getOrder(id: number): Promise<Order> {
  return apiClient.get<Order>(`/orders/${id}`);
}

export async function createOrder(input: Omit<Order, "id">): Promise<Order> {
  return apiClient.post<Order>("/orders", input);
}
