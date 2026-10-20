import { apiClient } from "../lib/apiClient";

export interface Review {
  id: number;
  productId: number;
  stars: number;
  body: string;
}

export async function getReview(id: number): Promise<Review> {
  return apiClient.get<Review>(`/reviews/${id}`);
}

export async function createReview(input: Omit<Review, "id">): Promise<Review> {
  return apiClient.post<Review>("/reviews", input);
}
