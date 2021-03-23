import motor.motor_asyncio
import os

# VERIFICA SE ESTÁ DENTRO DO DOCKER E ALTERA O NOME DO HOST
IN_DOCKER = os.environ.get('IN_DOCKER', False)
MONGO_DETAILS = f"mongodb://{'mongo' if IN_DOCKER else 'localhost'}:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.local

# Inicia as collections
endereco_collection = database.get_collection("endereco")
pessoa_collection = database.get_collection("pessoa")