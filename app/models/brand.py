from datetime import datetime

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.database.collections import BRANDS_COLLECTION


class Brand:
    collection_name = BRANDS_COLLECTION

    @staticmethod
    async def find_by_id(db: AsyncIOMotorDatabase, brand_id: ObjectId):
        """Find a brand by its ObjectId."""
        return await db[Brand.collection_name].find_one({"_id": brand_id})

    @staticmethod
    async def insert_brand(db: AsyncIOMotorDatabase, brand_data: dict):
        """Insert a new brand into the collection."""
        result = await db[Brand.collection_name].insert_one(brand_data)
        return result.inserted_id

    @staticmethod
    async def update_brand(db: AsyncIOMotorDatabase, brand_id: ObjectId, update_data: dict):
        """Update an existing brand."""
        return await db[Brand.collection_name].update_one({"_id": brand_id}, {"$set": update_data})

    @staticmethod
    async def delete_brand(db: AsyncIOMotorDatabase, brand_id: ObjectId):
        """Soft delete a brand by setting the `deleted_at` field."""
        return await db[Brand.collection_name].update_one({"_id": brand_id},
                                                          {"$set": {"deleted_at": datetime.utcnow()}})
