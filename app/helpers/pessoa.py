# Faz um parser no objeto Pessoa
def pessoa_helper(pessoa) -> dict:
	return {
		"id" : str(pessoa["_id"]),
		"nome" : pessoa["nome"],
		"idade" : pessoa["idade"],
		"endereco" : pessoa["endereco"],
	}