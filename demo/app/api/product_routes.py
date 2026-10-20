from app.db import get_db
from app.http import Request, Response, route
from app.services import product_service


@route("GET", "/products/{id}")
def show_product(request: Request) -> Response:
    product = product_service.get_product(get_db(), int(request.params["id"]))
    return Response.json(product.__dict__)


@route("POST", "/products")
def create_product(request: Request) -> Response:
    product = product_service.create_product(get_db(), request.json())
    return Response.json(product.__dict__, status=201)
