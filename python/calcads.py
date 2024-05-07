import numpy as np 

item = list ()
menu = True
VETOR_msculino = np.array([36,38,39,40,41,42,43])
VETOR_infantil = np.array([28,29,30,31])
VETOR_femino   = np.array([34,35,36,38,39,40])

def cadastro():

    print('-------cadastro de calcados----------')
    nome = input('nome :')
    dict_item = dict()
    dict_item['marca']      = input('marca: ')
    dict_item['quantidade'] = int (input('quandidade: '))
    dict_item['valor'] = float (input('valor: '))

    print('qual linha: 1 - infantil | 2 - Masculino |3 - feminino')
    lina = input('DIGITA: ')

    if lina == 1:
        dict_item['tamanho']    = VETOR_infantil
    elif lina == 2:
        dict_item['tamanho']    = VETOR_msculino
    else:
        dict_item['tamanho']    = VETOR_femino
    
    item.append({nome: dict_item})
    print('cadastro realizado !!!')

def venda():
        print('-------VENDA----------')
        nome = input('digite o nome do calcado: ')
        for i in range(len(item)):
            if nome in item[i]:
                print(item[i])
                quant = int (input('quantidade vendido: '))
                if item[i][nome]['quantidade'] >= quant:
                    item[i][nome]['quantidade'] -= quant
                    total = quant * item[i][nome]['valor']
                    print(f"{nome} vendidas com sucesso!")
                    print(f"quantidade: {quant}")
                    print(f"valor total: {total}")
                
            else:
                print(f"Desculpe, não temos {quant} unidades de {nome} disponíveis.")
            break
        else:
            print(f"Desculpe, o item {nome} não está disponível.")
    
def consutar():
    print('-------Consulta de Calçados----------')    
    for i in range(len(item)):
        print(item[i])
    
        
while(menu == True):

    print('---- menu-----')
    print(' 1 - CASATRAR MERCADORIA')
    print(' 2 - VENDA')
    print(' 3 - CONSUTAR')
    print(' 4 - ENCERRAR')
    OP = int(input('DIGITE OPÇÂO :'))

    if OP == 1:
        cadastro()    
    elif OP == 2:
        venda()
    elif OP == 3:
        consutar()
    elif OP == 4:
        menu = False
    else:
        print('OPÇÃO INVALIDA!!')

