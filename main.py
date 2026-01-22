from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import EmailStr, BaseModel

import uvicorn

from items_views import router as item_router
from users.views import router as users_router

app = FastAPI()
app.include_router(item_router)
app.include_router(users_router)



@app.get("/")
def hello_index():
    return{
        "message": "Hello index!",
    }

@app.get("/hello/")
def hello(name: str="World"):
    name=name.strip().title()
    return{"message": f"Hello {name}"}



@app.get("/calc/add/")
def add(a: int, b: int):
    return{
        "a": a,
        "b": b,
        "result": a + b,
    }


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)