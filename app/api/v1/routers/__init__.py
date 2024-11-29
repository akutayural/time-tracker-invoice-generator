from fastapi import APIRouter

from app.api.v1.routers.default import router as default_router
from app.api.v1.routers.user import router as user_router
from app.api.v1.routers.auth import router as auth_router

api_router = APIRouter()

# Include the api
api_router.include_router(router=default_router)
api_router.include_router(router=user_router)
api_router.include_router(router=auth_router)
