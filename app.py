# from fastapi import FastAPI
import uvicorn
from apps.main import create_app1

# app = FastAPI()

app = create_app1()

@app.get('/')
def _():    return "Hello, settings.uvicorn World1"


if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
