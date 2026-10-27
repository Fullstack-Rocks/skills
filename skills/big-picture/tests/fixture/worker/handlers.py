"""Fixture worker: consumes the app's order events."""


def subscribe(topic: str): return lambda handler: handler


@subscribe("order.created")
def send_receipt(event: dict) -> None:
    print("receipt for", event["order_id"])
