from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
import logging

from ..controllers.pessoa import (
  add_pessoa,
	get_pessoa,
	get_pessoas
)

from ..models.pessoa import (
  ErrorResponseModel,
	ResponseModel,
	PessoaSchema,
	CreatePessoaModel,
	PessoaResponseModel,
)

router = APIRouter()

@router.post("/", response_description="Dados de pessoa inseridos", response_model=PessoaResponseModel)
async def add_pessoa_data(pessoa: CreatePessoaModel = Body(...)):
	pessoa = jsonable_encoder(pessoa)
	new_pessoa = await add_pessoa(pessoa)
	return ResponseModel(new_pessoa, "Pessoa inserida com sucesso.")


@router.get("/", response_description="Pessoas retrieved", response_model=PessoaResponseModel)
async def get_pessoas():
    pessoas = await get_pessoas()
    if pessoas:
        return ResponseModel(pessoas, "Pessoas data retrieved successfully")
    return ResponseModel(pessoas, "Empty list returned")


@router.get("/{id}", response_description="Pessoa data retrieved", response_model=PessoaResponseModel)
async def get_pessoa_data(id):
    pessoa = await get_pessoa(id)
    if pessoa:
        return ResponseModel(pessoa, "Pessoa data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Pessoa doesn't exist.")