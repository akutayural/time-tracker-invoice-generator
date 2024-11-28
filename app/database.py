from mongoengine import connect
from config import configuration


# Establish a connection to MongoDB
def init_mongoengine():
    connect(
        db=configuration.MONGODB_DATABASE,
        host=configuration.MONGODB_URL,
        alias="default",  # Default alias for models
    )

