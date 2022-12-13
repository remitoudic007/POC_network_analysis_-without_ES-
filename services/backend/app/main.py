from typing import Union

from fastapi import FastAPI
from app.api import ping
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"ping": "pong!"}


app.include_router(ping.router)
