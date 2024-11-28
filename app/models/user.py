from mongoengine import StringField, DateField, ReferenceField, EnumField

from app.enums import UserRole, Status
from app.models.base import Base


class User(Base):
    meta = {"collection": "users"}

    first_name = StringField(required=True, max_length=64)
    last_name = StringField(required=True, max_length=64)
    birth_date = DateField()
    email = StringField(required=True, unique=True, max_length=320)
    username = StringField(required=True, unique=True, max_length=64)
    password = StringField(required=True, max_length=128)
    company_id = ReferenceField("Company", required=True)
    role = EnumField(UserRole, required=True, default=UserRole.TEAM_MEMBER)
    status = EnumField(Status, required=True, default=Status.ACTIVE)
