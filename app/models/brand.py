from mongoengine import StringField, URLField, BooleanField, ReferenceField
from app.models.base import Base



class Brand(Base):
    meta = {"collection": "brands"}  # Collection name for brands

    name = StringField(required=True, unique=True, max_length=128)  # Brand name
    company_id = ReferenceField("Company", required=True)  # Foreign key to Company
    domain = URLField(required=True, unique=True, max_length=128)  # Custom domain for the brand
    webhook_url = URLField(required=False, max_length=256)  # Optional webhook URL for integrations
    logo_url = URLField(required=False, max_length=256)  # Optional brand logo URL
    api_key = StringField(required=True, unique=True, max_length=64, null=False)  # Unique API key for the brand
    secret_key = StringField(required=True, unique=True, max_length=64)  # Unique secret key for the brand
    theme = StringField(required=False, max_length=64, default="default")  # Brand-specific theme (e.g., light, dark)
    subscription_id = ReferenceField("Subscription", required=True)  # Subscription for the brand
    support_email = StringField(required=True, max_length=320)  # Support email for the brand
    description = StringField(required=False, max_length=512)  # Optional brand description

