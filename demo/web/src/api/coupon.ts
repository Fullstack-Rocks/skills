import { apiClient } from "../lib/apiClient";

export interface Coupon {
  id: number;
  code: string;
  percentOff: number;
  active: boolean;
}

export async function getCoupon(id: number): Promise<Coupon> {
  return apiClient.get<Coupon>(`/coupons/${id}`);
}

export async function createCoupon(input: Omit<Coupon, "id">): Promise<Coupon> {
  return apiClient.post<Coupon>("/coupons", input);
}
