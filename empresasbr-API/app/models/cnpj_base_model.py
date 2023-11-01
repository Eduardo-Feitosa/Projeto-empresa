import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime

from .model_base import ModelBase
from .dominios_model import Natureza, Qualificacao, Cnaes, Motivos


# class PorteEmpresa(ModelBase):
#     __tablename__: str = 'porte_empresa'
    
#     CODIGO: str = sa.Column(sa.CHAR(1), primary_key=True, index=True)
#     DESCRICAO: str = sa.Column(sa.String(50), nullable=False)

#     def __repr__(self) -> str:
#         return f'<PorteEmpresa>'


class Empresas(ModelBase):
    __tablename__: str = 'empresas'

    CNPJ_BASE: str = sa.Column(sa.CHAR(8), primary_key=True, index=True)
    RAZAO_SOCIAL_NOME_EMPRESARIAL: str = sa.Column(sa.String(200))
    NATUREZA_JURIDICA: str = sa.Column(sa.CHAR(4), sa.ForeignKey('naturezas_juridicas.ID'))
    QUALIFICACAO_DO_RESPONSAVEL: str = sa.Column(sa.CHAR(2), sa.ForeignKey('qualificacoes_socios.ID'))
    CAPITAL_SOCIAL_DA_EMPRESA: float = sa.Column(sa.DECIMAL(14,2))
    PORTE_EMPRESA: str = sa.Column(sa.VARCHAR(30))
    ENTE_FEDERATIVO_RESPONSAVEL: str = sa.Column(sa.String(50))
    HASH: str = sa.Column(sa.VARCHAR(40))

    
    NATUREZA: orm.Mapped[Natureza] = orm.relationship('Natureza', lazy='joined')
    QUALIFICACAO: orm.Mapped[Qualificacao] = orm.relationship('Qualificacao', lazy='joined')

    def __repr__(self) -> str:
        return f'<Empresas>'


class Estabelecimentos(ModelBase):
    __tablename__: str = 'estabelecimentos'

    CNPJ: str = sa.Column(sa.CHAR(14), primary_key=True, index=True)
    CNPJ_BASICO: str = sa.Column(sa.CHAR(8), sa.ForeignKey('empresas.CNPJ_BASE'))
    CNPJ_ORDEM: str = sa.Column(sa.CHAR(4))
    CNPJ_DV: str = sa.Column(sa.CHAR(2))
    ID_MATRIZ_FILIAL: str = sa.Column(sa.VARCHAR(6))
    NM_FANTASIA: str = sa.Column(sa.VARCHAR(60))
    SITU_CADASTRAL: str = sa.Column(sa.VARCHAR(6))
    DT_SITU_CADASTRAL: datetime = sa.Column(sa.DATE)
    MT_SITU_CADASTRAL: str = sa.Column(sa.CHAR(2), sa.ForeignKey('motivos_situacao_empresa.ID'))
    CIDADE_EXTERIOR: str = sa.Column(sa.VARCHAR(60))
    PAIS: str = sa.Column(sa.CHAR(45))
    DT_INICIO_ATIV: datetime = sa.Column(sa.DATE)
    TP_LOGRADOURO: str = sa.Column(sa.VARCHAR(20))
    LOGRADOURO: str = sa.Column(sa.VARCHAR(100))
    NUMERO: int = sa.Column(sa.VARCHAR(10))
    COMPLEMENTO: str = sa.Column(sa.VARCHAR(200))
    BAIRRO: str = sa.Column(sa.VARCHAR(60))
    CEP: str = sa.Column(sa.CHAR(8))
    UF: str = sa.Column(sa.CHAR(2))
    MUNICIPIO: str = sa.Column(sa.CHAR(4))
    DDD1: str = sa.Column(sa.CHAR(4))
    TELEFONE1: str = sa.Column(sa.CHAR(8))
    DDD2: str = sa.Column(sa.CHAR(4))
    TELEFONE2: str = sa.Column(sa.CHAR(8))
    DDD_FAX: str = sa.Column(sa.CHAR(4))
    FAX: str = sa.Column(sa.CHAR(8))
    CORREIO_ELETRONICO: str = sa.Column(sa.VARCHAR(150))
    SITUACAO_ESPECIAL: str = sa.Column(sa.VARCHAR(50))
    DT_SITU_ESPECIAL: datetime = sa.Column(sa.DATE)
    HASH: str = sa.Column(sa.VARCHAR(40))

    ESTABELECIMENTOS_EMPRESAS_FK: orm.Mapped[Empresas] = orm.relationship('Empresas', lazy='joined')
    ESTABELECIMENTOS_MOTIVOS_FK: orm.Mapped[Motivos] = orm.relationship('Motivos', lazy='joined')

    def __repr__(self) -> str:
        return f'<Estabelecimentos>'
    

class Fiscal(ModelBase):
    __tablename__: str = 'fiscal'

    CNPJ: str = sa.Column(sa.CHAR(14), sa.ForeignKey('estabelecimentos.CNPJ'),primary_key=True)
    FISCAL: str = sa.Column(sa.CHAR(7), sa.ForeignKey('cnaes.ID'), primary_key=True)
    PRINCIPAL: int = sa.Column(sa.BOOLEAN)

    ESTABELECIMENTOS_FK: orm.Mapped[Estabelecimentos] = orm.relationship('Estabelecimentos', lazy='joined')
    FISCAL_FK: orm.Mapped[Cnaes] = orm.relationship('Cnaes', lazy='joined')

    def __repr__(self) -> str:
        return f'<Fiscal>'
    

class Socios(ModelBase):
    __tablename__: str = 'socios'

    ID: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    CNPJ_BASICO: str = sa.Column(sa.CHAR(8), sa.ForeignKey('empresas.CNPJ_BASE'))
    IDENTIFICADOR_SOCIO: str = sa.Column(sa.VARCHAR(20))
    NOME_SOCIO_OU_RAZAO_SOCIAL: str = sa.Column(sa.VARCHAR(150))
    CNPJ_CPF_SOCIO: str = sa.Column(sa.VARCHAR(14))
    QUALIFICACAO_SOCIO: str = sa.Column(sa.VARCHAR(100))
    DT_ENTRADA_SOCIEDADE: str = sa.Column(sa.DATE)
    PAIS: str = sa.Column(sa.VARCHAR(40))
    REPRESENTANTEA_LEGAL: str = sa.Column(sa.CHAR(11))
    NOME_REPRESENTANTE: str = sa.Column(sa.VARCHAR(100))
    QUALIFICACAO_REPRESENTANTE_LEGAL: str = sa.Column(sa.CHAR(2), sa.ForeignKey('qualificacoes_socios.ID'))
    FAIXA_ETARIA: str = sa.Column(sa.VARCHAR(20))
    HASH: str = sa.Column(sa.VARCHAR(40))

    ESTABELECIMENTOS_EMPRESAS_FK: orm.Mapped[Empresas] = orm.relationship('Empresas', lazy='joined')
    SOCIOS_QUALIFICACAO_FK: orm.Mapped[Qualificacao] = orm.relationship('Qualificacao', lazy='joined')

    def __repr__(self) -> str:
        return f'<Socios>'
