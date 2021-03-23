from bson.objectid import ObjectId
from ..config.database import pessoa_collection
from ..helpers.pessoa import pessoa_helper, parse_endereco_pessoa

# Retorna todas as pessoas
async def get_all_pessoas():
  pessoas = []
  async for pessoa in pessoa_collection.find():
    pessoas.append(pessoa_helper(pessoa))
  return pessoas


# Adiciona uma nova pessoa
async def add_pessoa(pessoa_data: dict) -> dict:
  pessoa_with_endereco = await parse_endereco_pessoa(pessoa_data)
  pessoa = await pessoa_collection.insert_one(pessoa_with_endereco)
  new_pessoa = await pessoa_collection.find_one({"_id": pessoa.inserted_id})
  return pessoa_helper(new_pessoa)


# Retorna uma pessoa por ID
async def get_pessoa(id: str) -> dict:
  pessoa = await pessoa_collection.find_one({"_id": ObjectId(id)})
  if pessoa:
    return pessoa_helper(pessoa)


# Atualiza uma pessoa por ID
async def update_pessoa(id: str, data: dict):
  # Retorna falso se não houver dados
  if len(data) < 1:
    return False
  pessoa = await pessoa_collection.find_one({"_id": ObjectId(id)})
  if pessoa:
    updated_pessoa = await pessoa_collection.update_one(
      {"_id": ObjectId(id)}, {"$set": data}
    )
    if updated_pessoa:
        return True
    return False


# Deleta uma pessoa por ID
async def delete_pessoa(id: str):
  pessoa = await pessoa_collection.find_one({"_id": ObjectId(id)})
  if pessoa:
    await pessoa_collection.delete_one({"_id": ObjectId(id)})
    return True