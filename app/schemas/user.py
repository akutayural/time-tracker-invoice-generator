from datetime import date
from typing import Optional
from pydantic import EmailStr, ConfigDict, BaseModel
from app.enums import UserRole, Status
from app.schemas.base import BaseSchema, PyObjectId


class UserSchema(BaseSchema):
    first_name: str
    last_name: str
    birth_date: Optional[date] = None
    email: EmailStr
    username: str
    password: str
    company_id: PyObjectId  # MongoDB ObjectId
    role: UserRole = UserRole.TEAM_MEMBER
    status: Status = Status.ACTIVE

    model_config = ConfigDict(from_attributes=True)


class CreateUserSchema(BaseModel):
    first_name: str
    last_name: str
    birth_date: Optional[date] = None
    email: EmailStr
    username: str
    password: str
    company_id: PyObjectId
    role: UserRole = UserRole.TEAM_MEMBER
    status: Status = Status.ACTIVE


class UpdateUserSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birth_date: Optional[date] = None
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None
    company_id: Optional[PyObjectId] = None
    role: Optional[UserRole] = None
    status: Optional[Status] = None
