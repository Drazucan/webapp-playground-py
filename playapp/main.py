from fastapi import FastAPI
from sqlmodel import SQLModel

from playapp import PlayAppLogger
from playapp.routes.v1 import users
from playapp.services.dbservice import PostgresClient, PostgresClientProvider

app = FastAPI()
logger = PlayAppLogger()

# Add the routes to the application
app.include_router(users.users_v1, prefix="/v1")
app.include_router(users.users_v1, prefix="/latest")

db = next(PostgresClientProvider.get_client())

def create_db_and_tables():
    SQLModel.metadata.create_all(db.get_engine())

app.add_event_handler("startup",create_db_and_tables)


@app.get("/")
async def hello():
    logger.info("User hit the HelloWorld endpoint")
    return {"message": "Hello World"}