from typing import Optional
from pydantic import EmailStr, HttpUrl, ConfigDict
from app.schemas.base import BaseSchema, PyObjectId


class BrandSchema(BaseSchema):
    name: str
    company_id: PyObjectId  # MongoDB ObjectId as a string
    domain: HttpUrl
    webhook_url: Optional[HttpUrl] = None
    logo_url: Optional[HttpUrl] = None
    api_key: str
    secret_key: str
    theme: Optional[str] = "default"
    subscription_id: PyObjectId  # MongoDB ObjectId as a string
    support_email: EmailStr
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
