import { apiClient } from "../lib/apiClient";

export interface Invoice {
  id: number;
  orderId: number;
  dueDays: number;
  paid: boolean;
}

export async function getInvoice(id: number): Promise<Invoice> {
  return apiClient.get<Invoice>(`/invoices/${id}`);
}

export async function createInvoice(input: Omit<Invoice, "id">): Promise<Invoice> {
  return apiClient.post<Invoice>("/invoices", input);
}
