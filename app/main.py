from fastapi import FastAPI
from .routes.endereco import router as EnderecoRouter
from .routes.pessoa import router as PessoaRouter

app = FastAPI()

app.include_router(EnderecoRouter, tags=["Endereco"], prefix="/endereco")
app.include_router(PessoaRouter, tags=["Pessoa"], prefix="/pessoa")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Wellcome!"}
