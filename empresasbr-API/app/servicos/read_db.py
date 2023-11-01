from app.bd.conexao_bd import create_engine, create_session

from app.models.cnpj_base_model import Estabelecimentos, Fiscal

from sqlalchemy.orm import selectinload


def read_empresa(cnpj_base: str):
    with create_engine().connect() as session:
        empresa = session.execute(text(f"""SELECT CNPJ_BASE, 
                                                  RAZAO_SOCIAL_NOME_EMPRESARIAL, 
                                                  NATUREZA_JURIDICA,
                                                  QUALIFICACAO_DO_RESPONSAVEL,
                                                  CAPITAL_SOCIAL_DA_EMPRESA,
                                                  PORTE_DA_EMPRESA,
                                                  ENTE_FEDERATIVO_RESPONSAVEL
                                           FROM empresas WHERE CNPJ_BASE = {cnpj_base}"""))

    linha = empresa.fetchone()
    if linha == None:
        return None

    return {
            "cnpj_base": linha[0],
            "razao_social_nome_empresarial": linha[1],
            "natureza_juridica": linha[2],
            "qualificacao_do_responsavel": linha[3],
            "capital_social_da_empresa": linha[4],
            "porte_da_empresa": linha[5],
            "ente_federativo_responsavel": linha[6]
        }


def read_estabelecimento(cnpj_id: str):

    with create_session() as session:
        cnpj = session.query(Estabelecimentos).filter(Estabelecimentos.CNPJ == cnpj_id).first()

    if cnpj is None:
        return None
    
    fiscal = session.query(Fiscal).filter(Fiscal.CNPJ == cnpj_id).all()

    cnae_fiscal_principal = None

    for item in fiscal:
        if item.PRINCIPAL == 1:
            cnae_fiscal_principal = item.FISCAL_FK.DESCRICAO
            break

    cnae_fiscal_secundaria = [item.FISCAL_FK.DESCRICAO for item in fiscal if item.PRINCIPAL == 0]

    return {"CNPJ": cnpj.CNPJ,
            "cnpj_basico": cnpj.CNPJ_BASICO,
            "cnpj_ordem": cnpj.CNPJ_ORDEM, 
            "cnpj_dv": cnpj.CNPJ_DV,
            "identificador_matriz_filial": cnpj.ID_MATRIZ_FILIAL,
            "nome_fantasia": cnpj.NM_FANTASIA,
            "situacao_cadastral": cnpj.SITU_CADASTRAL,
            "data_situacao_cadastral": cnpj.DT_SITU_CADASTRAL,
            "motivo_situacao_cadastral": cnpj.MT_SITU_CADASTRAL,
            "nome_da_cidade_no_exterior": cnpj.CIDADE_EXTERIOR,
            "pais": cnpj.PAIS,
            "data_de_inicio_atividade": cnpj.DT_INICIO_ATIV,
            "cnae_fiscal_principal": cnae_fiscal_principal,
            "cnae_fiscal_secundaria": cnae_fiscal_secundaria,
            "tipo_de_logradouro": cnpj.TP_LOGRADOURO,
            "logradouro": cnpj.LOGRADOURO,
            "numero": cnpj.NUMERO,
            "complemento": cnpj.COMPLEMENTO,
            "bairro": cnpj.BAIRRO,
            "cep": cnpj.CEP,
            "uf": cnpj.UF,
            "municipio": cnpj.MUNICIPIO,
            "ddd1": cnpj.DDD1,
            "telefone1": cnpj.TELEFONE1,
            "ddd2": cnpj.DDD2,
            "telefone2": cnpj.TELEFONE2,
            "ddd_do_fax": cnpj.DDD_FAX,
            "fax": cnpj.FAX,
            "correio_eletronico": cnpj.CORREIO_ELETRONICO,
            "situacao_especial": cnpj.SITUACAO_ESPECIAL,
            "data_da_situacao_especial": cnpj.DT_SITU_ESPECIAL}
