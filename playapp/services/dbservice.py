from sqlmodel import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy import Engine
from os import environ as env

from sqlalchemy.orm import sessionmaker, Session


class PostgresClient:
    """
    This class sets up a connection to a Postgres database by first attempting to genenrate a connection string given
    by environment variables, but falling back to defaults that should work in a local testing instance.
    """
    engine = create_engine(
        URL.create(
            drivername="postgresql",
            username=env.get("DB_USER", "postgres"),
            password=env.get("DB_PASSWORD", "password"),
            host=env.get("DB_HOST", "localhost"),
            port=env.get("DB_PORT", "5432"),
            database=env.get("DB_NAME", "postgres")
        ),
        pool_pre_ping=True
    )

    session_init = sessionmaker(autoflush=False, bind=engine)

    def __init__(self):
        self._session = self.session_init()

    def close(self):
        self._session.close()

    def get_session(self) -> Session:
        return self._session

    def get_engine(self) -> Engine:
        return self.engine


class PostgresClientProvider:
    """
    For use in FastAPI Depends scheme on endpoints for the application. The yield pattern below is described in the
    FastAPI documentation here: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#a-database-dependency-with-yieldv
    """
    @classmethod
    def get_client(cls) -> PostgresClient:
        db = PostgresClient()
        try:
            yield db
        finally:
            db.close()
