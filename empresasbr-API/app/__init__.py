from fastapi import FastAPI

from app.bd.conexao_bd import create_tables

from app.servicos.insert_db import create_estabelecimentos, create_motivos, create_empresas

from datetime import datetime

app = FastAPI()

create_tables()

create_empresas("12345678")

create_motivos(ID = "1", DESCRICAO = "teste")

create_estabelecimentos(

    CNPJ = "12345678910111",
    CNPJ_BASICO = "12345678",    
    CNPJ_ORDEM = "9101",
    CNPJ_DV = "11",
    ID_MATRIZ_FILIAL = "#######",
    NM_FANTASIA = "teste",
    SITU_CADASTRAL = "Teste",
    MT_SITU_CADASTRAL = "1", 
    CIDADE_EXTERIOR = "Brasilia",
    PAIS = "Brasil",
    DT_INICIO_ATIV = datetime.now(),
    DT_SITU_ESPECIAL = datetime.now(),
    HASH = "5456saffg564564fds65gf46fsd54g8fag4gff6g4")


from app.all_route import *
