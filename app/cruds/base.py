from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from bson.objectid import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=dict)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class AsyncCRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, collection: AsyncIOMotorCollection):
        """
        Async CRUD operations for a MongoDB collection.

        **Parameters**
        - `collection`: A Motor collection instance.
        """
        self.collection = collection

    async def get(self, id: Any) -> Optional[ModelType]:
        """Retrieve a single document by ID."""
        document = await self.collection.find_one({"_id": ObjectId(id)})
        return document

    async def get_multi(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """Retrieve multiple documents with optional pagination."""
        cursor = self.collection.find().skip(skip).limit(limit)
        return [doc async for doc in cursor]

    async def create(self, obj_in: CreateSchemaType) -> ModelType:
        """Create a new document."""
        obj_in_data = obj_in.dict()
        result = await self.collection.insert_one(obj_in_data)
        obj_in_data["_id"] = result.inserted_id
        return obj_in_data

    async def update(
        self,
        id: Any,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> Optional[ModelType]:
        """Update an existing document."""
        update_data = obj_in.dict(exclude_unset=True) if isinstance(obj_in, BaseModel) else obj_in
        result = await self.collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": update_data},
        )
        if result.modified_count == 1:
            return await self.get(id=id)
        return None

    async def remove(self, id: Any) -> Optional[ModelType]:
        """Delete a document by ID."""
        document = await self.get(id=id)
        if document:
            await self.collection.delete_one({"_id": ObjectId(id)})
        return document
