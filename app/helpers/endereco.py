# Faz um parser no objeto Endereco
def endereco_helper(endereco) -> dict:
	return {
		"cep": endereco["cep"],
		"logr": endereco["logr"],
		"compl": endereco["compl"],
		"bairro": endereco["bairro"],
		"cidade": endereco["cidade"],
		"uf": endereco["uf"],
	}

# Faz um aprser no objeto de resposta
def parse_response(res) -> dict:
	return {
		"cep": res["cep"].replace('-', ''),
		"logr": res["logradouro"],
		"compl": res["complemento"],
		"bairro": res["bairro"],
		"cidade": res["localidade"],
		"uf": res["uf"],
	}