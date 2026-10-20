import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    database_url: str
    payments_api_key: str
    smtp_host: str
    retention_days: int


def load_settings() -> Settings:
    return Settings(
        database_url=os.getenv("DATABASE_URL", "sqlite:///shop.db"),
        payments_api_key=os.environ["PAYMENTS_API_KEY"],
        smtp_host=os.environ.get("SMTP_HOST", "localhost"),
        retention_days=int(os.getenv("RETENTION_DAYS", "30")),
    )


settings = load_settings()
