"""Fixture events and live prices: the app publishes order events and pushes prices over a socket."""
from app.reports import order_total


def publish(topic: str, payload: dict) -> None: ...


class socket:
    @staticmethod
    def on(message: str): return lambda handler: handler

    @staticmethod
    def emit(message: str, payload: dict) -> None: ...


def announce_order(order_id: int) -> None:
    publish("order.created", {"order_id": order_id, "total_cents": order_total(order_id)})


@socket.on("subscribe")
def on_subscribe(payload: dict) -> None:
    push_price(payload["sku"])


def push_price(sku: str) -> None:
    socket.emit("price.update", {"sku": sku, "price_cents": 100})
