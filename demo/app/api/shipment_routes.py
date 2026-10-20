from app.db import get_db
from app.http import Request, Response, route
from app.services import shipment_service


@route("GET", "/shipments/{id}")
def show_shipment(request: Request) -> Response:
    shipment = shipment_service.get_shipment(get_db(), int(request.params["id"]))
    return Response.json(shipment.__dict__)


@route("POST", "/shipments")
def create_shipment(request: Request) -> Response:
    shipment = shipment_service.create_shipment(get_db(), request.json())
    return Response.json(shipment.__dict__, status=201)
