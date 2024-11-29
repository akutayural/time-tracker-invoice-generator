from fastapi import APIRouter, Depends, Path, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.cruds.user import user_crud
from app.schemas import ResponseModel
from app.schemas.user import CreateUserSchema, UserSchema

router = APIRouter(prefix="/user", tags=["User"])


@router.post("", response_model=ResponseModel)
async def create(user_in: CreateUserSchema):
    pass


@router.get("/{user_id}", response_model=ResponseModel[UserSchema])
async def get(user_id: int = Path()):
    pass




