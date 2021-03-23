from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from typing import List
import logging

from ..controllers.pessoa import (
  add_pessoa,
	get_pessoa,
	get_all_pessoas,
  delete_pessoa,
)

from ..models.pessoa import (
  ErrorResponseModel,
	ResponseModel,
	PessoaSchema,
	CreatePessoaModel,
)

router = APIRouter()


@router.post("/", response_description="Dados de pessoa inseridos", response_model=PessoaSchema)
async def add_pessoa_data(pessoa: CreatePessoaModel = Body(...)):
	pessoa = jsonable_encoder(pessoa)
	new_pessoa = await add_pessoa(pessoa)
	return new_pessoa


@router.get("/", response_description="Pessoas retornadas", response_model=List[PessoaSchema])
async def get_pessoas():
    pessoas = await get_all_pessoas()
    if pessoas:
        return pessoas
    return pessoas


@router.get("/{id}", response_description="Pessoa data retrieved", response_model=PessoaSchema)
async def get_pessoa_data(id):
    pessoa = await get_pessoa(id)
    if pessoa:
        return pessoa
    return ErrorResponseModel("An error occurred.", 404, "Pessoa doesn't exist.")


@router.delete("/{id}", response_description="Pessoa deletada do banco de dados")
async def delete_pessoa_data(id: str):
    deleted_pessoa = await delete_pessoa(id)
    if deleted_pessoa:
        return True
    return ErrorResponseModel(
        "An error occurred", 404, "Pessoa with id {0} doesn't exist".format(id)
    )


# @router.put("/{id}")
# async def update_pessoa_data(id: str, req: UpdatePessoaModel = Body(...)):
#     req = {k: v for k, v in req.dict().items() if v is not None}
#     updated_pessoa = await update_pessoa(id, req)
#     if updated_pessoa:
#         return ResponseModel(
#             "Pessoa with ID: {} name update is successful".format(id),
#             "Pessoa name updated successfully",
#         )
#     return ErrorResponseModel(
#         "An error occurred",
#         404,
#         "There was an error updating the pessoa data.",
#     )