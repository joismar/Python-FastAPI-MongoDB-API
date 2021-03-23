from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..controllers.endereco import (
    get_endereco,
)

from ..models.endereco import (
    ErrorResponseModel,
	ResponseModel,
    EnderecoResponseModel
)

router = APIRouter()

# Recebe um CEP e retorna um endereço
@router.get("/{cep}", response_description="CEP Recebido", response_model=EnderecoResponseModel)
async def get_endereco_data(cep):
    if cep:
        endereco = await get_endereco(cep)
        if endereco:
            return ResponseModel(endereco)
    return ErrorResponseModel(404, "Ocorreu um erro, talvez este CEP esteja inválido.")

