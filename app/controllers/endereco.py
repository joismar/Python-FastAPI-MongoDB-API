from ..config.database import endereco_collection
from ..helpers.endereco import endereco_helper, parse_response
import requests


async def get_endereco_from_cep(cep):
	res = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
	return parse_response(res.json())


async def add(endereco_data: dict) -> dict:
	endereco = await endereco_collection.insert_one(endereco_data)
	new_endereco = await endereco_collection.find_one({"_id": endereco.inserted_id})
	return endereco_helper(new_endereco)


async def get_endereco(cep) -> dict:
	endereco = await endereco_collection.find_one({"cep": cep})
	if endereco:
		return endereco_helper(endereco)
	data = await get_endereco_from_cep(cep)
	endereco = await add(data)
	return endereco
