from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    username: str
    email: str


class ResponseMessage(BaseModel):
    message: str


@router.post("/users", response_model=ResponseMessage, tags=["users"])
async def create_user():
    return {"message": "User received"}
