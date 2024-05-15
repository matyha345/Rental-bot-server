from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from src.config.setting import settings


def initialize_database():
    engine = create_engine(
        url=settings.DATABASE_URL_psycopg,
        echo=False,
        pool_size=5,
        max_overflow=10,
    )

    with engine.connect() as conn:
        result = conn.execute(text("SELECT VERSION()"))
        print(f"{result.all()=}")
        conn.commit()