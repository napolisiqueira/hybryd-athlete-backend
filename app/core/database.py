from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.mongodb_url)

async def db_connection():
    database = client[settings.database_name]
    return database

async def init_db():
    print("Conectado ao MongoDB:", settings.database_name)