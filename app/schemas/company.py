from typing import Optional

from pydantic import EmailStr, HttpUrl, ConfigDict
from app.schemas.base import BaseSchema, PyObjectId


class CompanySchema(BaseSchema):
    name: str
    email: EmailStr
    company_url: HttpUrl
    logo_url: Optional[HttpUrl] = None
    subscription: PyObjectId  # MongoDB ObjectId as a string

    model_config = ConfigDict(from_attributes=True)
