from mongoengine import StringField, URLField, ReferenceField
from app.models.base import Base


class Company(Base):
    meta = {"collection": "companies"}  # Specify the collection name for companies

    name = StringField(required=True, max_length=128)  # Unique company name
    email = StringField(required=True, unique=True, max_length=320)  # Email of the company admin
    company_url = URLField(required=True, max_length=256)  # Official URL of the company
    logo_url = URLField(required=False, max_length=256)  # Optional logo URL for the company
    subscription = ReferenceField("Subscription", required=True)  # Reference to the company's subscription
