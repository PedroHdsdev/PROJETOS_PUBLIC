import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyodbc
import pandas as pd

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class CamelCase:
    def __init__(self):
            self.conn = self.snake_case()
    def snake_case(self):
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
            messagebox.showinfo("erro de conexão",f"Erro ao conectar-se ao mysql:{err}")
            return None
    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            print("fechado!!","fechado!!")
    def chamar_tabela(self,qryselect):
        if self.conn:
            try:
                tabela = pd.read_sql(qryselect, self.conn)
                return tabela
            except pyodbc.Error as err:
                print(f"Erro ao chamar a tabela: {err}")
        return None
class principal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ERP MARCENARIA")
        self.banco = CamelCase()
        self.interface_login()
    
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def centralizar_janela(self, largura, altura):
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2
        self.geometry(f"{largura}x{altura}+{x}+{y}")

    def interface_login(self):
        for widget in self.winfo_children():
            widget.destroy() 

        largura_janela = 700
        altura_tela = 500

        self.centralizar_janela(largura_janela,altura_tela)

        frame = ctk.CTkFrame(self,bg_color = "transparent",fg_color="transparent")
        frame.grid(row=4, column=2, pady=10)

        ctk.CTkLabel(frame, text="Nome:",bg_color = "transparent").grid(row=1, column=1,columnspan = 1, pady=10, padx=5)
        self.usuario_entry = ctk.CTkEntry(frame,bg_color = "transparent")
        self.usuario_entry.grid(row=1, column=2, pady=5, padx=5)

        ctk.CTkLabel(frame, text="Senha:",bg_color = "transparent").grid(row=2, column=1,columnspan = 1, pady=10, padx=5)
        self.senha_entry = ctk.CTkEntry(frame, show="*",bg_color = "transparent")
        self.senha_entry.grid(row=2, column=2, pady=5, padx=10)

        ctk.CTkButton(frame, text="Entrar", command=self.realizar_login).grid(row=3, column=2, columnspan=1, pady=30,padx = 5)
        ctk.CTkButton(frame, text="Sair", command=self.fechar_login).grid(row=3, column=1, columnspan=1, pady=30,padx = 5)

    def interface_projetos(self):
        for widget in self.winfo_children():
            widget.destroy() 
        largura_janela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        self.tela_cheia()

        frame_menu = ctk.CTkFrame(self,bg_color = "transparent",fg_color="transparent")
        frame_menu.grid(row=1, column=2,columnspan = 1, pady=10,padx = 20,sticky="nsew")

        frame_pesquisa = ctk.CTkFrame(self,bg_color = "transparent",fg_color="transparent")
        frame_pesquisa.grid(row=2, column=2,columnspan = 1, pady=10,padx = 20,sticky="nsew")

        ctk.CTkButton(frame_menu, text="Cadastrar", command=self.ir_para_cadastro).grid(row=1, column=1, columnspan=1, pady=5,padx = 10)
        ctk.CTkButton(frame_menu, text="Deletar", command=self.realizar_login).grid(row=1, column=2, columnspan=1, pady=5,padx = 10)
        ctk.CTkButton(frame_menu, text="Atualizar", command=self.realizar_login).grid(row=1, column=3, columnspan=1, pady=5,padx = 10)
        ctk.CTkButton(frame_menu, text="Deletar", command=self.realizar_login).grid(row=1, column=4, columnspan=1, pady=5,padx = 10)
        
        ctk.CTkLabel(frame_pesquisa, text="Nome:",bg_color = "transparent").grid(row=1, column=1, pady=10, padx=10,sticky = "w")
        self.nome_entry = ctk.CTkEntry(frame_pesquisa,bg_color = "transparent",width= 500)
        self.nome_entry.grid(row=1, column=2, pady=10, padx=10, sticky = "w")
        ctk.CTkButton(frame_pesquisa, text="Pesquisar", command=self.realizar_login).grid(row=1, column=3, columnspan=1, pady=10 ,padx = 10,sticky = "w")

        ops_processos = ["DESENHO", "PLANO DE CORTE", "CORTE", "ACABAMENTO", "CORTE", "PRÉ MONTAGEM", "COMFERENCIA", "ESTOQUE","MONTAGEM/OBRA"]
        combobox_processo = ctk.CTkComboBox(frame_pesquisa, values= ops_processos,width=200)
        combobox_processo.set("Selecione uma opção")
        combobox_processo.grid(row=1, column=4,padx=10,pady=10,sticky = "w")

        self.radio_var = ctk.StringVar(value="EXECUÇÃO")
        self.radio_event()
        self.chama_tb_projeto()
        
    def interface_almoxerifado(self):

        self.tela_cheia()

        frame_menu = ctk.CTkFrame(self,bg_color = "transparent",fg_color="transparent")
        frame_menu.grid(row=1, column=2,columnspan = 1, pady=10,padx = 20,sticky="nsew")

        frame_pesquisa = ctk.CTkFrame(self,bg_color = "transparent",fg_color="transparent")
        frame_pesquisa.grid(row=2, column=2,columnspan = 1, pady=10,padx = 20,sticky="nsew")

        ctk.CTkButton(frame_menu, text="Cadastrar", command=self.ir_para_cadastro).grid(row=1, column=1, columnspan=1, pady=5,padx = 10)
        ctk.CTkButton(frame_menu, text="Deletar", command=self.realizar_login).grid(row=1, column=2, columnspan=1, pady=5,padx = 10)
        ctk.CTkButton(frame_menu, text="Pedidos de Compras", command=self.realizar_login).grid(row=1, column=3, columnspan=1, pady=5,padx = 10)
        ctk.CTkButton(frame_menu, text="Ferramentas em Usos", command=self.realizar_login).grid(row=1, column=4, columnspan=1, pady=5,padx = 10)
        
        ctk.CTkLabel(frame_pesquisa, text="Nome:",bg_color = "transparent").grid(row=1, column=1, pady=10, padx=10,sticky = "w")
        self.nome_entry = ctk.CTkEntry(frame_pesquisa,bg_color = "transparent",width= 500)
        self.nome_entry.grid(row=1, column=2, pady=10, padx=10, sticky = "w")
        ctk.CTkButton(frame_pesquisa, text="Pesquisar", command=self.realizar_login).grid(row=1, column=3, columnspan=1, pady=10 ,padx = 10,sticky = "w")
        
        if self.radio_var == "MATERIAPRIMA":
            ops_combobox = ["DESENHO", "PLANO DE CORTE", "CORTE", "ACABAMENTO", "CORTE", "PRÉ MONTAGEM", "COMFERENCIA", "ESTOQUE","MONTAGEM/OBRA"]
        else :
            ops_combobox = ["CORTE","FURAÇÃO","ACABAMENTO"]
            
        combobox_almoxerifado = ctk.CTkComboBox(frame_pesquisa, values= ops_combobox,width=200)
        combobox_almoxerifado.set("Selecione uma opção")
        combobox_almoxerifado.grid(row=1, column=4,padx=10,pady=10,sticky = "w")

        self.radio_var = ctk.StringVar(value="MATERIAPRIMA")
        self.radio_event()
        self.chama_tb_projeto()
     
    def radio_event(self):
        frame_Rdbutton = ctk.CTkFrame(self,bg_color = "transparent",fg_color="transparent")
        frame_Rdbutton.grid(row=3, column=2,columnspan = 1, pady=10,sticky="nsew")
            
        pass

        rdbutton_PJ_PRONTO = ctk.CTkRadioButton (frame_Rdbutton,text="PRONTO",command=self.radio_event,variable=self.radio_var,value="PRONTO")
        rdbutton_PJ_PRONTO.grid(row = 2, column = 1,columnspan = 1,pady = 10,padx = 10,sticky ="w")

        rdbutton_PJ_PRODUCAO = ctk.CTkRadioButton (frame_Rdbutton,text="PRODUÇÃO", command=self.radio_event,variable=self.radio_var,value="PRODUCAO")
        rdbutton_PJ_PRODUCAO.grid(row = 2, column = 2,columnspan = 1,pady = 10,padx = 10,sticky ="w")

        rdbutton_PJ_PARADO = ctk.CTkRadioButton (frame_Rdbutton,text="ESPERA",command=self.radio_event,variable=self.radio_var,value="ESPERA")
        rdbutton_PJ_PARADO.grid(row = 2, column = 3,columnspan = 1,pady = 10,padx = 10,sticky ="w")
        rdbutton_parado = ctk.CTkRadioButton (frame_Rdbutton,text="PARADO", command=self.radio_event,variable=self.radio_var,value="PARADO")
        rdbutton_parado.grid(row = 2, column = 3,columnspan = 1,pady = 10,padx = 10,sticky ="w")

            
        self.v = self.radio_var.get()

    def chama_tb_projeto(self):
                
        frame_tabela = ctk.CTkFrame(self,bg_color = "transparent",fg_color="transparent")
        frame_tabela.grid(row=4, column=2,columnspan = 3, pady=10,sticky="nsew")

        qryselect_projetos = "select*from VW_TELAPRINCIPAL_PROJETOS"
        tabela_pro_resultados =self.banco.chamar_tabela(qryselect_projetos)

        if tabela_pro_resultados is not None:
        # Convert pandas DataFrame to a list of lists
            data = tabela_pro_resultados.values.tolist()

            # Create the Treeview
            columns = tabela_pro_resultados.columns.tolist()
            self.tabela = ttk.Treeview(frame_tabela, columns=columns, show="headings", height=20,style = "Custom.Treeview")
            for coluna in columns:
                self.tabela.heading(coluna, text=coluna)
                self.tabela.column(coluna, width=200)

                # Insert data into the Treeview
            for row in data:
                self.tabela.insert("", tk.END, values=row)

            self.tabela.grid(row=1, column=2,columnspan = 2, sticky="nsew")

    def realizar_login(self):

        nome = self.usuario_entry.get()
        senha = self.senha_entry.get()
    
        if not nome or not senha:
            self.mostrar_mensagem_erro("Por favor, forneça nome de usuário e senha.")
            return
        qryselect_login = f"SELECT FUN_USUARIO, FUN_SENHA,CARG_ID FROM FUNCIONARIO WHERE FUN_USUARIO = '{nome}' AND FUN_SENHA = '{senha}'"
        resultado_login = self.banco.chamar_tabela(qryselect_login)

        if resultado_login is not None and not resultado_login.empty:
            carg_id = resultado_login['CARG_ID'].iloc[0] 
            # Usuário autenticado com sucesso, você pode redirecionar para a próxima tela ou realizar outras ações
            for widget in self.winfo_children():
                widget.destroy()
                self.withdraw()
            if carg_id == 1:
                self.interface_projetos()
            else:
                self.interface_almoxerifado()
        else:
            self.mostrar_mensagem_erro("senha ou usuario invalido !!")

    def mostrar_mensagem_erro(self, mensagem):
        if hasattr(self, "mensagem_erro_label"):
            self.erro_login_label.destroy()

        self.erro_login_label = ctk.CTkLabel(self, text=mensagem, text_color="red", bg_color="transparent")
        self.erro_login_label.grid(row=5, column=2, pady=10, padx=5)

    def fechar_login(self):
        self.destroy()

    def ir_para_cadastro(self):
        self.configurar_interface_cadastro()

    def voltar_para_login(self):
        self.configurar_interface_login()

    def tela_cheia(self):
        ##travar o tamanho da tela
        ##self.resizable(width=False, height=False)
        self.state('zoomed')

if __name__ == "__main__":
    app = principal()
    app.mainloop()
