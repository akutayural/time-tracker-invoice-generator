from datetime import datetime

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.database.collections import COMPANIES_COLLECTION


class Company:
    collection_name = COMPANIES_COLLECTION

    @staticmethod
    async def find_by_id(db: AsyncIOMotorDatabase, company_id: ObjectId):
        return await db[Company.collection_name].find_one({"_id": company_id})

    @staticmethod
    async def insert_company(db: AsyncIOMotorDatabase, company_data: dict):
        result = await db[Company.collection_name].insert_one(company_data)
        return result.inserted_id

    @staticmethod
    async def update_company(db: AsyncIOMotorDatabase, company_id: ObjectId, update_data: dict):
        return await db[Company.collection_name].update_one({"_id": company_id}, {"$set": update_data})

    @staticmethod
    async def delete_company(db: AsyncIOMotorDatabase, company_id: ObjectId):
        return await db[Company.collection_name].update_one({"_id": company_id},
                                                            {"$set": {"deleted_at": datetime.utcnow()}})
