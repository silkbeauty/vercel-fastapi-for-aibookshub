from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def _():    return "Hello, settings.uvicorn World"


if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
