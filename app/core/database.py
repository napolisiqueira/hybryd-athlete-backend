from beanie import init_beanie
from pymongo import AsyncMongoClient
from app.core.config import settings
from app.models.exercicios import Exercicio

client = AsyncMongoClient(settings.mongodb_url)

async def init_db():
    database = await db_connection()
    await init_beanie(database, document_models=[Exercicio])
    print("Conectado ao MongoDB", database.name)


async def db_connection():
    database = client[settings.database_name]
    return database

     