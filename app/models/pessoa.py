from typing import Optional
from pydantic import BaseModel, Field
from typing import List
from .endereco import EnderecoSchema
from bson.objectid import ObjectId


class PessoaSchema(BaseModel):

    id: str = Field(...)
    nome: str = Field(...)
    idade: int = Field(...)
    endereco: EnderecoSchema

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


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}