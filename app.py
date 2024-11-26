#app.py

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello_world():
    return "Hello,my World"


if __name__ == '__main__':
    import uvicorn
    # uvicorn.run(app)
    uvicorn.run(app, port=8080)