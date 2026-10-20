from app.db import get_db
from app.http import Request, Response, route
from app.services import invoice_service


@route("GET", "/invoices/{id}")
def show_invoice(request: Request) -> Response:
    invoice = invoice_service.get_invoice(get_db(), int(request.params["id"]))
    return Response.json(invoice.__dict__)


@route("POST", "/invoices")
def create_invoice(request: Request) -> Response:
    invoice = invoice_service.create_invoice(get_db(), request.json())
    return Response.json(invoice.__dict__, status=201)
