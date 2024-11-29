from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection
from pymongo.database import Database
from typing import Optional


class MongoDB:
    def __init__(self, db_url: str, db_name: str):
        self.client: Optional[AsyncIOMotorClient] = None
        self.db_url: str = db_url
        self.db_name: str = db_name
        self.db: Optional[Database] = None

    async def connect(self):
        """Establish a connection to MongoDB."""
        try:
            self.client = AsyncIOMotorClient(self.db_url)
            self.db = self.client[self.db_name]
        except Exception as e:
            raise RuntimeError(f"Failed to connect to MongoDB: {e}")

    async def disconnect(self):
        """Close the connection to MongoDB."""
        if self.client:
            self.client.close()

    def get_collection(self, collection_name: str) -> Collection:
        """Return a specific collection."""
        if not self.db:
            raise RuntimeError("Database connection is not established.")
        return self.db[collection_name]

    