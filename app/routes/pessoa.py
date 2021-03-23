from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from typing import List

from ..controllers.pessoa import (
  add_pessoa,
  get_pessoa,
  get_all_pessoas,
  delete_pessoa,
  update_pessoa,
)

from ..models.pessoa import (
  ErrorResponseModel,
  PessoaSchema,
  CreatePessoaModel,
  UpdatePessoaModel,
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


@router.get("/{id}", response_description="Dados da pessoa retornados", response_model=PessoaSchema)
async def get_pessoa_data(id):
  pessoa = await get_pessoa(id)
  if pessoa:
    return pessoa
  return ErrorResponseModel("Ocorreu um erro.", 404, "A pessoa não existe.")


@router.delete("/{id}", response_description="Pessoa deletada do banco de dados")
async def delete_pessoa_data(id: str):
  deleted_pessoa = await delete_pessoa(id)
  if deleted_pessoa:
    return {"Pessoa com id {} deletada com sucesso!".format(id)}
  return ErrorResponseModel(
    "Ocorreu um erro", 404, "Pessoa com o id {} não existe".format(id)
  )


@router.put("/{id}", response_model=PessoaSchema)
async def update_pessoa_data(id: str, req: UpdatePessoaModel = Body(...)):
  req = {k: v for k, v in req.dict().items() if v is not None}
  updated_pessoa = await update_pessoa(id, req)
  if updated_pessoa:
    return updated_pessoa
  return ErrorResponseModel("Ocorreu um erro", 404, "Ocorreu algum erro ao tentar ",
  )