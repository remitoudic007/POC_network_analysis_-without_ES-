from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
async def pong():
    # some async operation could happen here
    # example: `actors = await get_all_actors()`
    return {"ping": "pong!"}
