from pydantic import BaseModel, Field
from fastapi import HTTPException

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

class EnderecoResponseModel(BaseModel):
    sucesso: bool
    endereco: EnderecoSchema

    class Config:
        schema_extra = {
            "example": {
                "sucesso": True,
                "endereco": {
                    "cep" : "<cep>",
                    "logr" : "<logradouro>",
                    "compl" : "<complemento>",
                    "bairro" : "<bairro>",
                    "cidade" : "<cidade>",
                    "uf": "<uf>"
                }
            }
        }


def ResponseModel(data):
    return {
        "sucesso": True,
        "endereco": data
    }
    

def ErrorResponseModel(code, message):
    raise HTTPException(status_code=code, detail=message)