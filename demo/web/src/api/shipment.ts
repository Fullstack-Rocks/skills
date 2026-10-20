import { apiClient } from "../lib/apiClient";

export interface Shipment {
  id: number;
  orderId: number;
  carrier: string;
  tracking: string;
}

export async function getShipment(id: number): Promise<Shipment> {
  return apiClient.get<Shipment>(`/shipments/${id}`);
}

export async function createShipment(input: Omit<Shipment, "id">): Promise<Shipment> {
  return apiClient.post<Shipment>("/shipments", input);
}
