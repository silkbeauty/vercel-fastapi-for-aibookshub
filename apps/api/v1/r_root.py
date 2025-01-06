from fastapi import APIRouter

router = APIRouter()

@router.get('/test')
async def root(): return {"AIBooksHub": "New View Step by Step a, FastAPI!"}
