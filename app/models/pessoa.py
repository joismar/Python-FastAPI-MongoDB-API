from typing import Optional
from pydantic import BaseModel, Field
from typing import List
from .endereco import EnderecoSchema


class PessoaSchema(BaseModel):

    nome: str = Field(...)
    idade: int = Field(...)
    endereco: EnderecoSchema

    class Config:
        schema_extra = {
            "example": {
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
                "cep" : "50830460"
            }
        }

class UpdatePessoaModel(BaseModel):

    nome: Optional[str]
    idade: Optional[int]
    endereco: Optional[EnderecoSchema]

    class Config:
        schema_extra = {
            "example": {
                "nome" : "Example",
                "idade" : 42,
                "endereco" : {}
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


class PessoaResponseModel(BaseModel):

    data: List[PessoaSchema]
    code: int = Field(...)
    message: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "data": [
                    {
                        "nome" : "Example",
                        "idade" : 42,
                        "endereco" : {}
                    }
                ],
                "code": 200,
                "message": "Success!",
            }
        }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}