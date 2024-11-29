from datetime import datetime

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.database.collections import SUBSCRIPTIONS_COLLECTION


class Subscription:
    collection_name = SUBSCRIPTIONS_COLLECTION

    @staticmethod
    async def find_by_id(db: AsyncIOMotorDatabase, subscription_id: ObjectId):
        return await db[Subscription.collection_name].find_one({"_id": subscription_id})

    @staticmethod
    async def insert_subscription(db: AsyncIOMotorDatabase, subscription_data: dict):
        result = await db[Subscription.collection_name].insert_one(subscription_data)
        return result.inserted_id

    @staticmethod
    async def update_subscription(db: AsyncIOMotorDatabase, subscription_id: ObjectId, update_data: dict):
        return await db[Subscription.collection_name].update_one({"_id": subscription_id}, {"$set": update_data})

    @staticmethod
    async def delete_subscription(db: AsyncIOMotorDatabase, subscription_id: ObjectId):
        return await db[Subscription.collection_name].update_one({"_id": subscription_id},
                                                                 {"$set": {"deleted_at": datetime.utcnow()}})
