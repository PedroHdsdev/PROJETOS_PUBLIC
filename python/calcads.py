import numpy as np 

item    = list ()
menu    = True
v_cont  = 0
VETOR_msculino = np.array([36,38,39,40,41,42,43])
VETOR_infantil = np.array([28,29,30,31])
VETOR_femino   = np.array([34,35,36,38,39,40])

def cadastro(v_cont):

    print('-------cadastro de calçados----------')
    dict_item = dict()
    dict_item['codigo']     = v_cont    
    dict_item['nome']       = input('nome :')
    dict_item['marca']      = input('marca: ')
    dict_item['valor']      = float (input('valor: '))

    print('qual linha: 1 - Infantil | 2 - Feminino | 3 - Masculino ')
    lina = int(input('DIGITA: '))
    tamanho = dict()
    if lina == 1:
        dict_item['linha']      = 'Infantil'
        print(f'Tamanho para linha: {VETOR_infantil}')
    elif lina == 2:
        dict_item['linha']      = 'Feminino'
        print(f'Tamanho para linha: {VETOR_femino}')
    else:
        dict_item['linha']      = 'Masculino'
        print(f'Tamanho para linha: {VETOR_msculino}')

    v_tamanho               = int(input('digita numeração: '))
    tamanho[v_tamanho]      = int (input('quandidade: '))
    dict_item['tamanho']    = tamanho
    
    item.append(dict_item)
    print('cadastro realizado !!!')
    
    v_cont +=1
    return v_cont

def venda(): 
    print('-------calçados----------')
    for i in range(len(item)):
        print(item[i])
    
    print('-------cadastrar_venda----------')
    cod = int(input('digite o codigo do produto: '))
    tam = int(input('digite o tamanho do produto: '))
    
    if cod == item[i]['codigo']:
        if tam in item[i]['tamanho'] and item[i]['tamanho'][tam] > 0:
            quant = int (input('quantidade vendido: '))
            if item[i]['tamanho'][tam] >= quant:
                item[i]['tamanho'][tam] -= quant
                total = quant * item[i]['valor']

                print('-------VENDA----------')
                print(f'{item[i]['nome']} {item[i]['marca']} vendidas com sucesso!')
                print(f'tamanho: {tam}')
                print(f'quantidade: {quant}')
                print(f'valor total: {total}')
                    
            else:
                print(f"Desculpe, {item[i]['nome']} não tem {quant} unidades disponíveis.")
        else:
            print(f"Desculpe, o item {item[i]['nome']} não está disponível.")       
        
def consutar():
    print('-------Consulta de Calçados estoque----------')    
    for i in range(len(item)):
        print(item[i])
    
def alterar():
    print('-------Alterar Calçado----------')
    cod = int(input('Digite o código do produto que deseja alterar: '))
    for i in range(len(item)):
        if cod == item[i]['codigo']:
            print(f'Tamanho para linha: {item[i]['linha']}')
            if item[i]['linha'] == 'Infantil':
                    print(VETOR_infantil)
            elif item[i]['linha'] == 'Feminino':
                    print(VETOR_femino)
            else:
                    print(VETOR_msculino)
            tam = int(input('Digite o tamanho que deseja adicionar: '))
            quant = int(input('Digite a quantidade desse tamanho: '))
            if tam in item[i]['tamanho']:
                item[i]['tamanho'][tam] += quant
            else:                
                item[i]['tamanho'][tam] = quant
            print('Alteração realizada com sucesso!')
            break
    else:
        print(f"Desculpe, o item com o código {cod} não está disponível.")

while(menu == True):

    print('---- menu-----')
    print(' 1 - CASATRAR MERCADORIA')
    print(' 2 - VENDA')
    print(' 3 - CONSUTAR')
    print(' 4 - MUDAR A QUANTIDADE')
    print(' 5 - ENCERRAR')
    OP = int(input('DIGITE OPÇÂO :'))

    if OP == 1:
        v_cont = cadastro(v_cont)    
    elif OP == 2:
        venda()
    elif OP == 3:
        consutar()
    elif OP == 4:
        alterar()    
    elif OP == 5:
        menu = False
    else:
        print('OPÇÃO INVALIDA!!')
