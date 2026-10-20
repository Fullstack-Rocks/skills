from app.db import get_db
from app.http import Request, Response, route
from app.services import coupon_service


@route("GET", "/coupons/{id}")
def show_coupon(request: Request) -> Response:
    coupon = coupon_service.get_coupon(get_db(), int(request.params["id"]))
    return Response.json(coupon.__dict__)


@route("POST", "/coupons")
def create_coupon(request: Request) -> Response:
    coupon = coupon_service.create_coupon(get_db(), request.json())
    return Response.json(coupon.__dict__, status=201)
