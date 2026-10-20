import json
from dataclasses import dataclass, field
from typing import Callable

ROUTES: list[tuple[str, str, Callable]] = []


@dataclass
class Request:
    method: str
    path: str
    params: dict = field(default_factory=dict)
    body: bytes = b""

    def json(self) -> dict:
        return json.loads(self.body or b"{}")


@dataclass
class Response:
    body: str
    status: int = 200

    @classmethod
    def json(cls, data: dict, status: int = 200) -> "Response":
        return cls(json.dumps(data), status)


def route(method: str, path: str):
    def register(handler: Callable) -> Callable:
        ROUTES.append((method, path, handler))
        return handler
    return register
