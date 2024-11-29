from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field, ConfigDict, ValidationError
from typing import Optional


class PyObjectId(ObjectId):
    """Custom ObjectId type for Pydantic validation."""

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError(f"Invalid ObjectId: {value}")
        return str(value)


class BaseSchema(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")  # MongoDB's primary key
    created_at: datetime = Field(default_factory=datetime.utcnow, frozen=True)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    deleted_at: Optional[datetime] = None

    model_config = ConfigDict(
        from_attributes=True,  # Allow creation from attributes (ORM-like)
        arbitrary_types_allowed=True,  # Enable custom types like PyObjectId
        json_encoders={ObjectId: str},  # Use `str` when serializing ObjectId
    )
