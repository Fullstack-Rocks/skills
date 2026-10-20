import { apiClient } from "../lib/apiClient";

export interface Warehouse {
  id: number;
  city: string;
  capacity: number;
  open: boolean;
}

export async function getWarehouse(id: number): Promise<Warehouse> {
  return apiClient.get<Warehouse>(`/warehouses/${id}`);
}

export async function createWarehouse(input: Omit<Warehouse, "id">): Promise<Warehouse> {
  return apiClient.post<Warehouse>("/warehouses", input);
}
