import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str
    price: float


class User(BaseModel):
    username: str
    email: str


class HelloMessage(BaseModel):
    Hello: str


class ResponseMessage(BaseModel):
    message: str


@app.get("/", response_model=HelloMessage, tags=["root"])
def read_root():
    return {"Hello": "World"}


@app.post("/items/", response_model=ResponseMessage, tags=["items"])
async def create_item():
    return {"message": "Item received"}


@app.get("/items/", response_model=list[Item], tags=["items"])
async def get_items():
    return [
        {"name": "Plumbus", "price": 3},
        {"name": "Portal Gun", "price": 9001},
    ]


@app.post("/users/", response_model=ResponseMessage, tags=["users"])
async def create_user():
    return {"message": "User received"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
