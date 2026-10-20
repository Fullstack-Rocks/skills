import { apiClient } from "../lib/apiClient";

export interface Product {
  id: number;
  sku: string;
  priceCents: number;
  stock: number;
}

export async function getProduct(id: number): Promise<Product> {
  return apiClient.get<Product>(`/products/${id}`);
}

export async function createProduct(input: Omit<Product, "id">): Promise<Product> {
  return apiClient.post<Product>("/products", input);
}
