from typing import Union

from fastapi import FastAPI
from app.api import ping
from fastapi import FastAPI

app = FastAPI()

# add router ....


@app.get("/")
def read_root():
    return {"ping": "pong!"}


@app.get("/platform_user")
def read_root():
    return {"ping": "pong!"}


@app.get("/actors ")
def read_root():
    return {"ping": "pong!"}


app.include_router(ping.router)
