import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # MongoDB
    MONGODB_DATABASE: str = "time-tracker"
    MONGODB_URL: str = "mongodb://localhost:27017"
    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0

    # Kafka
    KAFKA_BROKER: str = "localhost:9092"
    ZOOKEEPER_HOST: str = "localhost:2181"


configuration = Settings()
