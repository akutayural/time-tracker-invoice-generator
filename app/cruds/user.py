from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.cruds.base import AsyncCRUDBase
from app.schemas.user import CreateUserSchema, UpdateUserSchema


class UserCRUD(AsyncCRUDBase[User, CreateUserSchema, UpdateUserSchema]):
    async def get_by_username(self, db: AsyncSession, username: str):
        result = await db.execute(select(User).filter(User.username == username))
        return result.scalar_one_or_none()


user_crud = UserCRUD(collection=User)
