from datetime import datetime

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.database.collections import USERS_COLLECTION


class User:
    collection_name = USERS_COLLECTION

    @staticmethod
    async def find_by_id(db: AsyncIOMotorDatabase, user_id: ObjectId):
        return await db[User.collection_name].find_one({"_id": user_id})

    @staticmethod
    async def insert_user(db: AsyncIOMotorDatabase, user_data: dict):
        result = await db[User.collection_name].insert_one(user_data)
        return result.inserted_id

    @staticmethod
    async def update_user(db: AsyncIOMotorDatabase, user_id: ObjectId, update_data: dict):
        return await db[User.collection_name].update_one({"_id": user_id}, {"$set": update_data})

    @staticmethod
    async def delete_user(db: AsyncIOMotorDatabase, user_id: ObjectId):
        return await db[User.collection_name].update_one({"_id": user_id}, {"$set": {"deleted_at": datetime.utcnow()}})
