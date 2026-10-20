from app.db import get_db
from app.http import Request, Response, route
from app.services import warehouse_service


@route("GET", "/warehouses/{id}")
def show_warehouse(request: Request) -> Response:
    warehouse = warehouse_service.get_warehouse(get_db(), int(request.params["id"]))
    return Response.json(warehouse.__dict__)


@route("POST", "/warehouses")
def create_warehouse(request: Request) -> Response:
    warehouse = warehouse_service.create_warehouse(get_db(), request.json())
    return Response.json(warehouse.__dict__, status=201)
