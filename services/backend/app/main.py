
from app.api import ping, user

from fastapi import FastAPI

app = FastAPI()
app.include_router(ping.router)
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"POC Fastapi Backend": "Actor Based Neo4j"}
