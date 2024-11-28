from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from mongoengine import Document

ModelType = TypeVar("ModelType", bound=Document)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A MongoEngine model class
        """
        self.model = model

    def get(self, id: Any) -> Optional[ModelType]:
        """Retrieve a single document by ID."""
        return self.model.objects(id=id).first()

    def get_multi(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """Retrieve multiple documents with optional pagination."""
        return list(self.model.objects.skip(skip).limit(limit))

    def create(self, obj_in: CreateSchemaType) -> ModelType:
        """Create a new document."""
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # Create a new instance of the model
        db_obj.save()  # Save to the database
        return db_obj

    def update(
        self,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> ModelType:
        """Update an existing document."""
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in update_data:
            if field in obj_data:
                setattr(db_obj, field, update_data[field])
        db_obj.save()  # Save the changes to the database
        return db_obj

    def remove(self, id: Any) -> Optional[ModelType]:
        """Delete a document by ID."""
        obj = self.model.objects(id=id).first()
        if obj:
            obj.delete()  # Delete the document
        return obj