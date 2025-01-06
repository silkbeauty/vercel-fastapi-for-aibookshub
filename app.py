import uvicorn

from apps.config import settings
from apps import main

app = main.create_app(settings)

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
