from app.database.mongodb import MongoDB
from pymongo.collection import Collection

# Collection names
USERS_COLLECTION = "users"
COMPANIES_COLLECTION = "companies"
BRANDS_COLLECTION = "brands"
SUBSCRIPTIONS_COLLECTION = "subscriptions"


class Collections:
    def __init__(self, db: MongoDB):
        self.db = db

    def users(self) -> Collection:
        return self.db.get_collection(USERS_COLLECTION)

    def companies(self) -> Collection:
        return self.db.get_collection(COMPANIES_COLLECTION)

    def brands(self) -> Collection:
        return self.db.get_collection(BRANDS_COLLECTION)

    def subscriptions(self) -> Collection:
        return self.db.get_collection(SUBSCRIPTIONS_COLLECTION)
