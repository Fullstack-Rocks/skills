from app.db import get_db
from app.http import Request, Response, route
from app.services import review_service


@route("GET", "/reviews/{id}")
def show_review(request: Request) -> Response:
    review = review_service.get_review(get_db(), int(request.params["id"]))
    return Response.json(review.__dict__)


@route("POST", "/reviews")
def create_review(request: Request) -> Response:
    review = review_service.create_review(get_db(), request.json())
    return Response.json(review.__dict__, status=201)
