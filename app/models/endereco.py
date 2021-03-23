from typing import Optional
from pydantic import BaseModel, Field


class EnderecoSchema(BaseModel):

    cep: str = Field(...)
    logr: str = Field(...)
    compl: str = Field(...)
    bairro: str = Field(...)
    cidade: str = Field(...)
    uf: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "cep" : "<cep>",
                "logr" : "<logradouro>",
                "compl" : "<complemento>",
                "bairro" : "<bairro>",
                "cidade" : "<cidade>",
                "uf": "<uf>"
            }
        }


class UpdateEnderecoModel(BaseModel):

    cep: Optional[str]
    logr: Optional[str]
    compl: Optional[str]
    bairro: Optional[str]
    cidade: Optional[str]
    uf: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "cep" : "<cep>",
                "logr" : "<logradouro>",
                "compl" : "<complemento>",
                "bairro" : "<bairro>",
                "cidade" : "<cidade>",
                "uf": "<uf>"
            }
        }


def ResponseModel(data):
    return {
        "sucesso": True,
        "endereco": [data]
    }
    

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}