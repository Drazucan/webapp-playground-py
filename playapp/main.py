from fastapi import FastAPI
from playapp import PlayAppLogger
from playapp.routes.v1alpha1 import users_v1alpha1


app = FastAPI()
logger = PlayAppLogger()

# Add the routes to the application
app.include_router(users_v1alpha1.router, prefix="/v1alpha1")
app.include_router(users_v1alpha1.router, prefix="/latest")


@app.get("/")
async def hello():
    logger.info("User hit the HelloWorld endpoint")
    return {"message": "Hello World"}