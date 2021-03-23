from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..controllers.endereco import (
    get_endereco,
)

from ..models.endereco import (
    ErrorResponseModel,
	ResponseModel,
)

router = APIRouter()

@router.get("/{cep}", response_description="CEP Recebido!")
async def get_endereco_data(cep):
    endereco = await get_endereco(cep)
    if endereco:
        return ResponseModel(endereco)
    return ErrorResponseModel("An error occurred.", 404, "Cep inválido.")

