from app.db import get_db
from app.http import Request, Response, route
from app.services import order_service


@route("GET", "/orders/{id}")
def show_order(request: Request) -> Response:
    order = order_service.get_order(get_db(), int(request.params["id"]))
    return Response.json(order.__dict__)


@route("POST", "/orders")
def create_order(request: Request) -> Response:
    order = order_service.create_order(get_db(), request.json())
    return Response.json(order.__dict__, status=201)


@route("POST", "/orders/{id}/pay")
def pay_order(request: Request) -> Response:
    import os
    api_key = os.getenv("PAYMENTS_API_KEY")
    order = order_service.get_order(get_db(), int(request.params["id"]))
    return Response.json({"order": order.id, "charged": bool(api_key)})
