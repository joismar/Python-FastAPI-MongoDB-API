<h1 align="center">Python FastAPI MongoDB API</h1>

<p align="center">
  <img alt="Principal linguagem do projeto" src="https://img.shields.io/github/languages/top/joismar/python-fastapi-mongodb-api?color=56BEB8">

  <img alt="Quantidade de linguagens utilizadas" src="https://img.shields.io/github/languages/count/joismar/python-fastapi-mongodb-api?color=56BEB8">

  <img alt="Tamanho do repositório" src="https://img.shields.io/github/repo-size/joismar/python-fastapi-mongodb-api?color=56BEB8">

  <img alt="Licença" src="https://img.shields.io/github/license/joismar/python-fastapi-mongodb-api?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/joismar/python-fastapi-mongodb-api?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/joismar/python-fastapi-mongodb-api?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/joismar/python-fastapi-mongodb-api?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Python FastAPI MongoDB API 🚀 Em construção...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-sobre">Sobre</a> &#xa0; | &#xa0; 
  <a href="#sparkles-funcionalidades">Funcionalidades</a> &#xa0; | &#xa0;
  <a href="#rocket-tecnologias">Tecnologias</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-pré-requesitos">Pré requisitos</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-começando">Começando</a> &#xa0; | &#xa0;
  <a href="#memo-licença">Licença</a> &#xa0; | &#xa0;
  <a href="https://github.com/joismar" target="_blank">Autor</a>
</p>

<br>

## :dart: Sobre ##

O projeto a seguir implementa uma API em Python com uso de FastAPI e MongoDB como banco de dados.

## :sparkles: Funcionalidades ##

:heavy_check_mark: API de consultar CEP, onde dado um CEP retornará os dados de endereço a partir de uma API pública;\
:heavy_check_mark: CRUD de uma entidade Pessoa integrada a API de CEP;\
:heavy_check_mark: Persistência dos dados em MongoDB;\
:heavy_check_mark: Documentação automática em SwaggerUI seguindo os padrões do FastAPI;
:heavy_check_mark: Containerização para fast deploy.

## :rocket: Dependências ##

Os seguintes módulos e ferramentas foram usados na construção do projeto:

- [FastAPI](https://fastapi.tiangolo.com/)
- [PyMongo](https://pymongo.readthedocs.io/en/stable/)
- [Motor](https://pypi.org/project/motor/)
- [Uvicorn](https://www.uvicorn.org/)
- [Requests](https://requests.readthedocs.io/en/master/)

## :white_check_mark: Pré requisitos ##

Antes de começar :checkered_flag:, você precisa ter o [Git](https://git-scm.com), [Python](https://www.python.org/) 3.7 ou superior instalados em sua maquina ou em uma virtual env e um [MongoDB](https://www.mongodb.com/) local instalado ou em docker, nesse projeto você só precisará executar o comando ```docker-compose up``` na raiz do projeto.

## :checkered_flag: Começando ##

#### Primeiro...
```bash
# Clone este repositório
$ git clone https://github.com/joismar/python-fastapi-mongodb-api

# Entre na pasta
$ cd python-fastapi-mongodb-api

# Crie a pasta do mongodb para usar com docker (somente se não tiver instalado localmente)
$ mkdir mongodb/database
```
#### Rodando... (com docker)
Descomente as linhas correspondentes a API no arquivo docker-compose.yml
```bash
# Execute o comando abaixo e... Pronto!
$ docker-compose up -d

# O app vai inicializar em <http://localhost:8080>
```
#### Rodando... (com dependency manager)
```bash
# Subir mongodb no docker
$ docker-compose up -d

# Instale as dependências (com poetry)
$ poetry install
# Ou use o requirements.txt para usar o seu gerenciador de dependencias preferido

# Para iniciar o projeto
$ poetry shell
$ > uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
# Caso não esteja usando o poetry, execute o comando acima na raiz do projeto
# remova o "--reload" para produção

# O app vai inicializar em <http://localhost:8080>
```
#### Testando a API
Abra http://localhost:8080/docs em seu navegador e realize os testes 😁/
## :memo: Licença ##

Este projeto está sob licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.


Feito com :heart: por <a href="https://github.com/joismar" target="_blank">Joismar Braga</a>

&#xa0;

<a href="#top">Voltar para o topo</a>
