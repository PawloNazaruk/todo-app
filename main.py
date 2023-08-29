
# Todo List Application made with FastAPI

from fastapi import FastAPI
import uvicorn

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
