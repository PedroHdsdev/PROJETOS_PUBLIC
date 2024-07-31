-- DDL --
CREATE DATABASE ERP_MARCENARIA
DROP DATABASE ERP_MARCENARIA
USE ERP_MARCENARIA
--------------- RH -----------------------
CREATE TABLE ESTADO(
EST_ID			INT IDENTITY (1,1)NOT NULL,
EST_NOME		VARCHAR(50)NOT NULL,
EST_SIGLA		VARCHAR(2)NOT NULL,
CONSTRAINT EST_ID PRIMARY KEY (EST_ID),
CONSTRAINT EST_UNIQUE_NOME UNIQUE (EST_NOME),
CONSTRAINT EST_UNIQUE_SIGLA UNIQUE (EST_SIGLA)
)

CREATE TABLE DEPARTAMENTO(
DEP_ID		INT IDENTITY (1,1)NOT NULL,
DEP_NOME	VARCHAR(50)NOT NULL,
CONSTRAINT DEP_ID PRIMARY KEY (DEP_ID),
CONSTRAINT DEP_UNIQUE_NOME UNIQUE (DEP_NOME)
)

CREATE TABLE CIDADE(
CID_ID			INT IDENTITY (1,1)NOT NULL,
CID_NOME		VARCHAR(50) NOT NULL,
CID_CEP			VARCHAR(20) NOT NULL,
EST_ID			INT NOT NULL,
CONSTRAINT CID_ID PRIMARY KEY (CID_ID),
CONSTRAINT fK_EST_ID FOREIGN KEY (EST_ID) REFERENCES ESTADO(EST_ID),
CONSTRAINT CID_UNIQUE_NOME UNIQUE (CID_NOME)
)

CREATE TABLE CARGO(
CARG_ID					INT IDENTITY (1,1)NOT NULL,
CARG_NOME				VARCHAR(50)NOT NULL,
CARG_SALARIOBASE		DECIMAL(18,2)NOT NULL,
DEP_ID					INT NOT NULL,
CONSTRAINT CARG_ID	PRIMARY KEY (CARG_ID),
CONSTRAINT fK_DEP_ID FOREIGN KEY (DEP_ID) REFERENCES DEPARTAMENTO(DEP_ID),
CONSTRAINT CARG_UNIQUE_NOME UNIQUE (CARG_NOME)
)

CREATE TABLE FUNCIONARIO(
FUN_ID				INT IDENTITY (1,1) NOT NULL,
FUN_NOME			VARCHAR(50) NOT NULL,
FUN_USUARIO			VARCHAR(20)NULL,
FUN_SENHA			VARCHAR(16)NULL,
FUN_SALARIO			DECIMAL(10,2)NOT NULL,
FUN_RG				VARCHAR(11)NULL,
FUN_CPF				VARCHAR(11)NULL,
FUN_DATA_ADMISSAO	DATE NOT NULL,
FUN_DATA_NACIMENTO	DATE NOT NULL,
FUN_ENDERECO		VARCHAR(50)NOT NULL,
CID_ID				INT NOT NULL,
CARG_ID				INT NOT NULL,
CONSTRAINT FUN_ID PRIMARY KEY (FUN_ID),
CONSTRAINT fK_CID_ID FOREIGN KEY (CID_ID) REFERENCES CIDADE(CID_ID),
CONSTRAINT fK_CARG_ID FOREIGN KEY (CARG_ID) REFERENCES CARGO(CARG_ID),
CONSTRAINT FUN_UNIQUE_RG UNIQUE (FUN_RG),
CONSTRAINT FUN_UNIQUE_NOME UNIQUE (FUN_NOME),
CONSTRAINT FUN_UNIQUE_CPF UNIQUE (FUN_CPF),
CONSTRAINT FUN_UNIQUE_USUARIO UNIQUE (FUN_USUARIO),
CONSTRAINT FUN_UNIQUE_SENHA UNIQUE (FUN_SENHA)
)
-------------- OPERACIONAL ------------------

CREATE TABLE CLIENTE(
CLI_ID				INT IDENTITY (1,1)NOT NULL,
CLI_NOME			VARCHAR(50)NOT NULL,
CLI_CNPJ			VARCHAR(14)NULL,
CLI_EDERECO			VARCHAR(50)NOT NULL,
CID_ID				INT NOT NULL,
CONSTRAINT CLI_ID PRIMARY KEY (CLI_ID),
CONSTRAINT fK_CLI_CID_ID FOREIGN KEY (CID_ID) REFERENCES CIDADE(CID_ID),
CONSTRAINT CLI_UNIQUE_NOME UNIQUE (CLI_NOME),
CONSTRAINT CLI_UNIQUE_CNPJ UNIQUE (CLI_CNPJ),
)

CREATE TABLE OBRAS(
OBR_ID					INT IDENTITY (1,1)NOT NULL,
OBR_NOME				VARCHAR(50)NOT NULL,
OBR_ENDERECO			VARCHAR(50)NOT NULL,
OBR_ANDAR				VARCHAR(10)NULL,
OBR_NM_APARTAMENTO		VARCHAR(10)NULL,
OBR_INF_ELEVADOR		VARCHAR(50)NULL,
OBR_INF_ESCADA			VARCHAR(50)NULL,
OBR_INF_ESTACIONAMENTO	VARCHAR(10)NULL,
OBRA_OBSERVACAO			VARCHAR(200)NULL,
CID_ID					INT NOT NULL,
CONSTRAINT OBR_ID	PRIMARY KEY (OBR_ID),
CONSTRAINT fK_OBR_CID_ID FOREIGN KEY (CID_ID) REFERENCES CIDADE(CID_ID)
)

CREATE TABLE AMBIENTE(
AMB_ID				INT IDENTITY (1,1)NOT NULL,
AMB_NOME			VARCHAR(50)NOT NULL,
AMB_LARGURA			INT NOT NULL,
AMB_COMPRIMENTO		INT NOT NULL,
AMB_ALTURA			INT NOT NULL,
AMB_QUANT_TOMADA	INT NULL,
AMB_QUANT_PORTAS	INT NULL,
AMB_QUANT_JANELAS	INT NULL,
AMB_PDF				VARBINARY(MAX),
AMB_INFORMACAO		VARCHAR(255)NULL,
OBR_ID				INT NOT NULL,
CONSTRAINT AMB_ID PRIMARY KEY (AMB_ID),
CONSTRAINT fK_AMB_OBR_ID FOREIGN KEY (OBR_ID) REFERENCES OBRAS(OBR_ID)
)

CREATE TABLE INF_PAREDE (
IPAR_ID					INT IDENTITY (1,1) NOT NULL,
IPAR_REFERENCIA			VARCHAR(50)NOT NULL,
IPAR_TIPO_PAREDE        VARCHAR(50) NOT NULL,
IPAR_COR                VARCHAR(50)NULL,
IPAR_TEXTURA            VARCHAR(50)NULL,
IPAR_ALTURA             DECIMAL(10,2)NULL,
IPAR_LARGURA            DECIMAL(10,2)NULL,
IPAR_POSICAO_X          DECIMAL(10,2)NULL,
IPAR_POSICAO_Y          DECIMAL(10,2)NULL,
IPAR_OUTRAS_INFORMACOES VARCHAR(MAX)NULL,
AMB_ID              INT NOT NULL,
CONSTRAINT IPAR_ID PRIMARY KEY (IPAR_ID),
CONSTRAINT FK_INFO_AMB_ID FOREIGN KEY (AMB_ID) REFERENCES AMBIENTE(AMB_ID)
)

CREATE TABLE PROJETOS(
PRO_ID				INT IDENTITY (1,1)NOT NULL,
PRO_NOME			VARCHAR(50)NOT NULL,
PRO_DATA_INICIO		DATE NOT NULL,
PRO_DATA_ENTREGA	DATE NOT NULL,
PRO_DATA_TERMINO	DATETIME NULL,
PRO_MQUADRADOTOTAL	DECIMAL(10,2),
PRO_STATUS			VARCHAR(50)NOT NULL,
OBR_ID				INT NOT NULL,
CLI_ID				INT NOT NULL,
CONSTRAINT PRO_ID PRIMARY KEY (PRO_ID),
CONSTRAINT FK_PRO_OBR_ID FOREIGN KEY (OBR_ID) REFERENCES OBRAS(OBR_ID),
CONSTRAINT FK_PRO_CLI_ID FOREIGN KEY (CLI_ID) REFERENCES CLIENTE(CLI_ID),
CONSTRAINT PRO_STATUS_CHEQUE CHECK (PRO_STATUS IN ('PRONTO','ESPERA','PRODU플O'))
)

CREATE TABLE MODULOS(
MOD_ID				INT IDENTITY (1,1)NOT NULL,
MOD_NOME			VARCHAR(25)NOT NULL,
MOD_SIGLA			VARCHAR(10)NOT NULL,
MOD_MQUADRADO		DECIMAL(10,2)NOT NULL,
MOD_DESCRI플O		VARCHAR(255)NULL,
MOD_STATUS			VARCHAR(50)NULL,
MOD_PROCESSO		VARCHAR(50)NULL,
MOD_DATA_INICIO		DATE NULL,
MOD_DARA_TERMINO	DATE NULL,
MOD_PDF				VARBINARY(MAX)NULL,
PRO_ID				INT NOT NULL,
CONSTRAINT MOD_ID PRIMARY KEY (MOD_ID),
CONSTRAINT MOD_STATUS_CHEQUE CHECK (MOD_STATUS IN ('PRONTO','ESPERA','PRODU플O')),
CONSTRAINT MOD_PROCESSO_CHEQUE CHECK (MOD_PROCESSO IN ('GERA플O DE PLANO DE CORTE','CORTE','ACABAMENTO','USINAGEM','PRE MONTAGEM','COMFERENCIA/EMBALAGEM','ESTOQUE','MONTAGEM/OBRA'))
)

CREATE TABLE FUNCIONARIO_MODULO(
FM_ID			INT IDENTITY (1,1)NOT NULL,
FUN_ID			INT NOT NULL,
MOD_ID			INT NOT NULL,
CONSTRAINT FM_ID PRIMARY KEY (FM_ID),
CONSTRAINT FK_FM_FUN_ID FOREIGN KEY (FUN_ID) REFERENCES FUNCIONARIO(FUN_ID),
CONSTRAINT FK_FM_MOD_ID FOREIGN KEY (MOD_ID) REFERENCES MODULOS(MOD_ID)
)

-------------- ALMOXERIFADO ------------------

CREATE TABLE MATERIA_PRIMA(
MP_ID				INT IDENTITY (1,1)NOT NULL,
MP_NOME				VARCHAR(50) NOT NULL,		
MP_QUANTIDADE		INT NOT NULL,
MP_DATA_VALIDADE	DATE NULL,
MP_PESO				DECIMAL(10,2) NULL,
MP_LARGURA			DECIMAL(10,2) NULL,
MP_COMPRIMENTO		DECIMAL(10,2) NULL,
MP_ESPESSURA		DECIMAL(10,2) NULL,
MP_LAGURA			DECIMAL(10,2) NULL,
MP_COR				VARCHAR(50)NULL,
MP_PROPRIEDADE		VARCHAR(80)NULL,
MP_DESCRICAO		VARCHAR(100)NULL,
MP_LOCAL			VARCHAR(100)NULL,
CONSTRAINT MP_ID PRIMARY KEY (MP_ID)
)

CREATE TABLE FERRAMENTAS(
FER_ID				INT IDENTITY(1,1)NOT NULL,
FER_NOME			VARCHAR(50)NOT NULL,
FER_MODELO			VARCHAR(50)NOT NULL,
FER_VOTAGEM			VARCHAR(4)NOT NULL,
FER_QUANTIDADE		INT NOT NULL,
FER_CONDICAO		VARCHAR(50)NULL,
FER_OBSERVACAO		VARCHAR(255)NULL,
FER_STATUS			VARCHAR(50) NOT NULL,
CONSTRAINT FER_ID PRIMARY KEY (FER_ID),
CONSTRAINT FER_CONDICAO_CHEQUE CHECK (FER_CONDICAO IN ('NOVA','SEMI NOVA','USADA','GASTA')),
CONSTRAINT FER_STATUS_CHEQUE CHECK (FER_STATUS IN ('ESTOQUE','MANUTEN플O','EM USO'))
)

CREATE TABLE FORNECEDOR(
FOR_ID			INT IDENTITY (1,1)NOT NULL,
FOR_NOME		VARCHAR(50) NOT NULL,
FOR_ENDERECO	VARCHAR(50) NOT NULL,
FOR_CNPJ		VARCHAR(14) NULL,
CID_ID			INT NOT NULL,
CONSTRAINT FOR_ID PRIMARY KEY (FOR_ID),
CONSTRAINT FK_FOR_CID_ID FOREIGN KEY (CID_ID) REFERENCES CIDADE(CID_ID),
CONSTRAINT FOR_UNIQUE_NOME UNIQUE (FOR_NOME), 
CONSTRAINT FOR_UNIQUE_CNPJ UNIQUE (FOR_CNPJ)
)

CREATE TABLE H_MANUTENCAO(
MAN_ID				INT IDENTITY (1,1)NOT NULL,
MAN_DATA_ENTRADA	DATE NOT NULL,
MAN_DARA_SAIDA		DATE NULL,
MAN_DESCRICAO		VARCHAR(200) NULL,
MAN_VALOR			DECIMAL(10,2) NULL,
FER_ID				INT NOT NULL,
CONSTRAINT MAN_ID PRIMARY KEY (MAN_ID),
CONSTRAINT FK_FER_ID FOREIGN KEY (FER_ID) REFERENCES FERRAMENTAS(FER_ID)
)

CREATE TABLE PEDIDOS(
PED_ID				INT IDENTITY (1,1)NOT NULL,
PED_QUANT_TOTAL		INT NOT NULL,
PED_DATA_PEDIDO		DATE NOT NULL,
PED_DATA_ENTREGA	DATE NULL,
PED_VALOR_TOTAL		DECIMAL(10,2) NULL,
PED_STATUS			VARCHAR(50) NOT NULL,
FOR_ID				INT NOT NULL,
FUN_ID				INT NOT NULL,
CONSTRAINT PED_ID PRIMARY KEY (PED_ID),
CONSTRAINT FK_PED_FOR_ID FOREIGN KEY (FOR_ID) REFERENCES FORNECEDOR(FOR_ID),
CONSTRAINT FK_PED_FUN_ID FOREIGN KEY (FUN_ID) REFERENCES FUNCIONARIO(FUN_ID),
CONSTRAINT PED_CONDICAO_CHEQUE CHECK (PED_STATUS IN('ANALIZE','COMPRA','FINALIZADO'))
)

CREATE TABLE PEDIDOS_MATERIA_PRIMA(
PED_MP_ID				INT IDENTITY (1,1)NOT NULL,
PED_MP_QUANT_UNITARIO	INT NOT NULL,
PED_MP_VALORUNITARIO	DECIMAL (10,2)NOT NULL,
PED_ID					INT NOT NULL,
MP_ID					INT NOT NULL,
CONSTRAINT PED_MP_ID PRIMARY KEY (PED_MP_ID),
CONSTRAINT FK_PM_PED_ID FOREIGN KEY (PED_ID) REFERENCES PEDIDOS(PED_ID),
CONSTRAINT FK_PM_MP_ID FOREIGN KEY (MP_ID) REFERENCES MATERIA_PRIMA(MP_ID)
)
--- FAZER UMA CONDI플O PARA FERRAMENTAS NOVAS TRIGGER IF (FERRAMENTA = O / CADASTRAR -> TABELA FERRAMENTAS) ELSE (FERRAMENTA > 0 / SOMAR) --
CREATE TABLE PEDIDOS_FERRAMENTAS(
PED_FER_ID				INT IDENTITY (1,1)NOT NULL,
PED_FER_QUANT_UNITARIO	INT NOT NULL,
PED_FER_VALORUNITARIO	DECIMAL (10,2)NOT NULL,
PED_ID					INT NOT NULL,
FER_ID					INT NOT NULL,
CONSTRAINT PED_FER_ID PRIMARY KEY (PED_ID),
CONSTRAINT FK_PF_PED_ID FOREIGN KEY (PED_ID) REFERENCES PEDIDOS(PED_ID),
CONSTRAINT FK_PF_FER_ID FOREIGN KEY (FER_ID) REFERENCES FERRAMENTAS(FER_ID)
)

CREATE TABLE H_USO_MATERIA_PRIMA(
HMP_ID						INT IDENTITY (1,1)NOT NULL,
HMP_QUANTIDADE				INT NOT NULL,
HMP_DATA_RETIRADA			DATETIME NOT NULL,
HMP_DATA_DEVOLUCAO			DATETIME NULL,
CONSTRAINT HMP_ID PRIMARY KEY (HMP_ID)
)

CREATE TABLE H_USO_FERRAMENTAS(
HFER_ID						INT IDENTITY (1,1)NOT NULL,
HFER_QUANTIDADE				INT NOT NULL,
HFER_DATA_RETIRADA			DATETIME NOT NULL,
HFER_DATA_DEVOLUCAO			DATETIME NULL,
CONSTRAINT HFER_ID PRIMARY KEY (HFER_ID)
)

CREATE TABLE HUSO_MATERIA_PRIMA(
HUSO_MP_ID					INT IDENTITY (1,1)NOT NULL,
HMP_ID						INT NOT NULL,
MP_ID						INT NOT NULL,
CONSTRAINT HUSO_MP_ID PRIMARY KEY (HUSO_MP_ID),
CONSTRAINT FK_HUSO_MP_ID FOREIGN KEY (MP_ID) REFERENCES MATERIA_PRIMA(MP_ID),
CONSTRAINT FK_HUSO_HMP_ID FOREIGN KEY (HMP_ID) REFERENCES H_USO_MATERIA_PRIMA(HMP_ID)
)

CREATE TABLE HUSO_FERRAMENTAS(
HUSO_FER_ID					INT IDENTITY (1,1)NOT NULL,
HFER_ID						INT NOT NULL,
FER_ID						INT NOT NULL,
CONSTRAINT HUSO_FER_ID PRIMARY KEY (HUSO_FER_ID),
CONSTRAINT FK_HUSO_HFER_ID FOREIGN KEY (HFER_ID) REFERENCES H_USO_FERRAMENTAS(HFER_ID),
CONSTRAINT FK_HUSO_FER_ID FOREIGN KEY (FER_ID) REFERENCES FERRAMENTAS(FER_ID)
)

CREATE TABLE CONTATOS(
CONT_ID				INT IDENTITY(1,1)NOT NULL,
CONT_CELULAR		VARCHAR(15)NOT NULL,
CONT_TELEFONE		VARCHAR(15)NULL,
CONT_COMERCIAL		VARCHAR(15)NULL,
CONT_EMAIL			VARCHAR(50)NOT NULL,
FUN_ID				INT NULL,
CLI_ID				INT NULL,
FOR_ID				INT NULL,
CONSTRAINT CONT_ID PRIMARY KEY (CONT_ID),
CONSTRAINT fK_CONT_FUN_ID FOREIGN KEY (FUN_ID) REFERENCES FUNCIONARIO(FUN_ID),
CONSTRAINT fK_CONT_CLI_ID FOREIGN KEY (CLI_ID) REFERENCES CLIENTE(CLI_ID),
CONSTRAINT fK_CONT_FOR_ID FOREIGN KEY (FOR_ID) REFERENCES FORNECEDOR(FOR_ID),
CONSTRAINT CONT_UNIQUE_CELULAR UNIQUE (CONT_CELULAR),
CONSTRAINT CONT_UNIQUE_TELEFONE UNIQUE (CONT_TELEFONE),
CONSTRAINT CONT_UNIQUE_COMERCIAL UNIQUE (CONT_COMERCIAL),
CONSTRAINT CONT_UNIQUE_EMAIL UNIQUE (CONT_EMAIL)
)



-- ALMOXARIFADO
DROP TABLE HUSO_FERRAMENTAS;
DROP TABLE HUSO_MATERIA_PRIMA;
DROP TABLE H_USO_FERRAMENTAS;
DROP TABLE H_USO_MATERIA_PRIMA;
DROP TABLE PEDIDOS_FERRAMENTAS;
DROP TABLE PEDIDOS_MATERIA_PRIMA;
DROP TABLE PEDIDOS;
DROP TABLE H_MANUTENCAO;
DROP TABLE FORNECEDOR;
DROP TABLE FERRAMENTAS;
DROP TABLE MATERIA_PRIMA;

-- OPERACIONAL
DROP TABLE FUNCIONARIO_MODULO;
DROP TABLE MODULOS;
DROP TABLE PROJETOS;
DROP TABLE INF_PAREDE;
DROP TABLE AMBIENTE;
DROP TABLE OBRAS;
DROP TABLE CLIENTE;

-- RH
DROP TABLE CONTATOS;
DROP TABLE FUNCIONARIO;
DROP TABLE CARGO;
DROP TABLE DEPARTAMENTO;
DROP TABLE CIDADE;
DROP TABLE ESTADO;