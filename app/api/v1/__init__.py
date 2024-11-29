from fastapi import APIRouter
from app.api.v1.routers import auth, user

v1_router = APIRouter()
v1_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
v1_router.include_router(user.router, prefix="/users", tags=["Users"])

