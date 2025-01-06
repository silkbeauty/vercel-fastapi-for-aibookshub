import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.api import router 

app = FastAPI()

app.include_router(router)



if __name__ == '__main__':
    # uvicorn.run(app, port=8080)
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
