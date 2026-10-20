from app.db import get_db
from app.http import Request, Response, route
from app.services import customer_service


@route("GET", "/customers/{id}")
def show_customer(request: Request) -> Response:
    customer = customer_service.get_customer(get_db(), int(request.params["id"]))
    return Response.json(customer.__dict__)


@route("POST", "/customers")
def create_customer(request: Request) -> Response:
    customer = customer_service.create_customer(get_db(), request.json())
    return Response.json(customer.__dict__, status=201)
