from app import app

from datetime import datetime

from app.servicos.read_db import read_empresa,read_estabelecimento


@app.get("/api/v1/empresas/{empresa}")
async def consultar_empresa(empresa: str):

    return {"datetime": datetime.now(),
            "message": read_empresa(empresa),
            "status": 200}

@app.get("/api/v1/estabelecimentos/{cnpj}")
async def consultar_estabelecimento(cnpj:str):
    return {
        "datetime":datetime.now(),
        "message":read_estabelecimento(cnpj),
        "status":200
    }
