from fastapi import APIRouter
router = APIRouter()

@router.get("/platform_user", tags=["neo4j"] )
def platformusers():
    return {"ping": "pong!"}

