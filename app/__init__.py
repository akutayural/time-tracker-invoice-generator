from fastapi import FastAPI
from app.helpers.logging import Logging

logger = Logging(name="app-log").get_logger()
request_logger = Logging(name="request-log").get_logger()


from app.database import init_mongoengine
from app.routers import api_router

# Create the FastAPI application
app = FastAPI(title="API")

# Include the main API router
app.include_router(router=api_router)

# Initialize the database connection
init_mongoengine()


# Log all registered routes
for route in app.routes:
    print(f"Route: {route.path} | Methods: {route.methods}")
