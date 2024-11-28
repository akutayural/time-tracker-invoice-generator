from mongoengine import DateTimeField, ReferenceField, EnumField

from app.enums.subscription import SubscriptionPlan
from app.models.base import Base
from app.enums import Status


class Subscription(Base):
    meta = {"collection": "subscriptions"}  # Collection name for subscriptions

    company_id = ReferenceField("Company", required=True)  # Foreign key to Company
    plan_name = EnumField(SubscriptionPlan, required=True, default=SubscriptionPlan.BASIC)  # Name of the subscription plan
    start_date = DateTimeField(required=True)  # Subscription start date
    end_date = DateTimeField(required=True)  # Subscription end date
    status = EnumField(Status, required=True, default=Status.ACTIVE)  # Subscription status

