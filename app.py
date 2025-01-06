from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def _():    return "Hello,uvicorn Worlddd"


if __name__ == '__main__':
    # uvicorn.run(app, port=8080)
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
