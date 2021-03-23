from ..controllers.endereco import get_endereco

def pessoa_helper(pessoa) -> dict:
	return {
		"id" : str(pessoa["_id"]),
		"nome" : pessoa["nome"],
		"idade" : pessoa["idade"],
		"endereco" : pessoa["endereco"],
	}

async def parse_endereco_pessoa(pessoa) -> dict:
	endereco = {}
	
	if pessoa['cep']:
		endereco = await get_endereco(pessoa['cep'])

	return {
		"nome" : pessoa["nome"],
		"idade" : pessoa["idade"],
		"endereco" : endereco,
	}