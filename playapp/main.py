from fastapi import FastAPI
from playapp import PlayAppLogger


app = FastAPI()
logger = PlayAppLogger()

@app.get("/")
async def hello():
    logger.info("User hit the HelloWorld endpoint")
    return {"message": "Hello World"}