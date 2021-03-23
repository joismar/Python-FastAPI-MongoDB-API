from ..config.database import endereco_collection
from ..helpers.endereco import endereco_helper, parse_response
import requests

# Faz uma requisição na API e retorna um endereço
async def get_endereco_from_cep(cep):
	res = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
	return parse_response(res.json())


# Insere um endereço na base de dados
async def add(endereco_data: dict) -> dict:
	endereco = await endereco_collection.insert_one(endereco_data)
	new_endereco = await endereco_collection.find_one({"_id": endereco.inserted_id})
	return endereco_helper(new_endereco)


# Recebe um CEP e retorna um endereço
async def get_endereco(cep) -> dict:
	endereco = await endereco_collection.find_one({"cep": cep})
	if endereco:
		return endereco_helper(endereco)
	try:
		data = await get_endereco_from_cep(cep)
	except:
		return False
	endereco = await add(data)
	return endereco
