
# Todo List Application made with FastAPI

from fastapi import FastAPI
import uvicorn

import models
from database import engine
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router, prefix="/api/tasks")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
