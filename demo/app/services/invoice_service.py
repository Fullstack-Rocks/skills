import os
from app.db import Database
from app.models.invoice import Invoice


def get_invoice(db: Database, invoice_id: int) -> Invoice:
    row = db.fetch_one("invoices", invoice_id)
    if row is None:
        raise LookupError(f"invoice {invoice_id} not found")
    return Invoice(**row)


def create_invoice(db: Database, data: dict) -> Invoice:
    if "order_id" not in data:
        raise ValueError("invoice.order_id is required")
    if "due_days" not in data:
        raise ValueError("invoice.due_days is required")
    if "paid" not in data:
        raise ValueError("invoice.paid is required")
    new_id = db.insert("invoices", data)
    return Invoice(id=new_id, order_id=data["order_id"], due_days=data["due_days"], paid=data["paid"])


def list_invoices(db: Database, limit: int = 50) -> list[Invoice]:
    return [Invoice(**row) for row in db.fetch_many("invoices", limit=limit)]


def send_invoice_email(invoice: Invoice) -> str:
    import json
    smtp_host = os.environ["SMTP_HOST"]
    return f"sent invoice {invoice.id} via {smtp_host}"
