import os

from app.db import get_db
from app.http import Request, Response, route
from app.services import loyalty_service


@route("GET", "/customers/{id}/loyalty")
def show_loyalty(request: Request) -> Response:
    rate = float(os.environ.get("LOYALTY_RATE", "0.05"))
    row = get_db().fetch_one("customers", int(request.params["id"]))
    if row is None:
        return Response.json({"points": 0})
    if row["tier"] == "gold":
        rate = rate * 2
    points = loyalty_service.points_for(row, rate)
    return Response.json({"points": points})
