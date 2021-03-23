from typing import Optional
from pydantic import BaseModel, Field
from .endereco import EnderecoSchema
from fastapi import HTTPException

class PessoaSchema(BaseModel):

    id: str = Field(...)
    nome: str = Field(...)
    idade: int = Field(...)
    endereco: EnderecoSchema = {}

    class Config:
        schema_extra = {
            "example": {
                "id" : "hash",
                "nome" : "Example",
                "idade" : 42,
                "endereco" : {}
            }
        }


class CreatePessoaModel(BaseModel):

    nome: str = Field(...)
    idade: int = Field(...)
    cep: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "nome" : "Example",
                "idade" : 42,
                "cep" : "15046250"
            }
        }

class UpdatePessoaModel(BaseModel):

    nome: Optional[str]
    idade: Optional[int]
    cep: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "nome" : "Example",
                "idade" : 42,
                "cep" : "15046250"
            }
        }


def ErrorResponseModel(code, message):
    raise HTTPException(status_code=code, detail=message)