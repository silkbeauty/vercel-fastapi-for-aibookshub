from fastapi import FastAPI
import uvicorn
from apps.config import settings


app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
)


@app.get('/')
def _():    return "Hello,uvicorn Worlddd"


if __name__ == '__main__':
    # uvicorn.run(app, port=8080)
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
