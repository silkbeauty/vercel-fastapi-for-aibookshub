from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def _():    return "Hello, Worlddd"

@router.get('/test')
async def root(): return {"AIBooksHub": "New View Step by Step a, FastAPI!"}



