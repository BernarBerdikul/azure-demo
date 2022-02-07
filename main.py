import uvicorn
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

# load environment variables
port = os.getenv("PORT")
# initialize FastAPI
app = FastAPI()


@app.get("/v1/")
def index_v1():
    return {"data": "Application ran successfully - FastAPI"}


@app.get("/v2/")
def index_v2():
    return {"data": "Application ran successfully - FastAPI release v2.0"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)

