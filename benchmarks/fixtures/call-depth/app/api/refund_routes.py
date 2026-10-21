from app.db import get_db
from app.http import Request, Response, route
from app.services import refund_service


@route("POST", "/orders/{id}/refund")
def refund_order(request: Request) -> Response:
    body = request.json()
    receipt = refund_service.refund(get_db(), int(request.params["id"]), body["reason"])
    return Response.json(receipt)
