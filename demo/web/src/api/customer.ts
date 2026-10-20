import { apiClient } from "../lib/apiClient";

export interface Customer {
  id: number;
  email: string;
  name: string;
  tier: string;
}

export async function getCustomer(id: number): Promise<Customer> {
  return apiClient.get<Customer>(`/customers/${id}`);
}

export async function createCustomer(input: Omit<Customer, "id">): Promise<Customer> {
  return apiClient.post<Customer>("/customers", input);
}
