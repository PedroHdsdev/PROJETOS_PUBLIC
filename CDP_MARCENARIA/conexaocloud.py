import pyodbc
from tkinter import ttk, messagebox

class ConexaoSQLServer:
    def __init__(self):
            self.conn = self.connect_banco()
    def connect_banco(self):
        try:
            server = 'DESKTOP-23EGHLN\SQLEXPRESS'
            database = 'ERP_MARCENARIA'
            username = 'ERP'
            password = 'ERP123'
            driver = '{ODBC Driver 17 for SQL Server}'

            conn = pyodbc.connect(f'SERVER={server};DATABASE={database};UID={username};PWD={password};DRIVER={driver}')
            print("sucesso!!","sucesso!!!")
            return conn
        except pyodbc.Error as err:
            print("erro de conexão",f"Erro ao conectar-se ao mysql:{err}")
            return None
    def chamar_tabela(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT*FROM ESTADO")
                resultados = cursor.fetchall()
                return resultados
            except pyodbc.Error as err:
                print(f"Erro ao chamar a tabela: {err}")
        return None
    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
 
conexao = ConexaoSQLServer()

dados_da_tabela = conexao.chamar_tabela()

if dados_da_tabela:
    for linha in dados_da_tabela:
        print(linha)


conexao.fechar_conexao()