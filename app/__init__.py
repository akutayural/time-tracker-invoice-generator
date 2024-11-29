from fastapi import FastAPI

import config
from app.database.mongodb import MongoDB
from app.database.collections import Collections
from app.helpers.logging import Logging

logger = Logging(name="app-log").get_logger()
request_logger = Logging(name="request-log").get_logger()

from app.api import api_router

# Create the FastAPI application
app = FastAPI(title="API")

# Include the main API router
app.include_router(router=api_router)

# Initialize MongoDB connection
mongodb = MongoDB(db_url=config.configuration.MONGODB_URL,
                  db_name=config.configuration.MONGODB_DATABASE)

# Global variable to hold collections
collections: Collections = None


def get_collections() -> Collections:
    """Return the initialized collections instance."""
    if collections is None:
        raise RuntimeError("Collections are not initialized.")
    return collections


@app.on_event("startup")
async def startup_event():
    """Connect to MongoDB on app startup."""
    global collections
    await mongodb.connect()
    collections = Collections(mongodb)  # Initialize collections
    logger.info("MongoDB connected and collections initialized.")


@app.on_event("shutdown")
async def shutdown_event():
    """Disconnect from MongoDB on app shutdown."""
    await mongodb.disconnect()
    logger.info("MongoDB connection closed.")

