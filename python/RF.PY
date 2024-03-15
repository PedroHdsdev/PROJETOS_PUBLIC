import requests


# URL da API
def getinformacao():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

    response = requests.get(url)
    MOED = response.json()
    print(MOED.json())
    USD_BRL = MOED['CODE']['BID']
    
    print(USD_BRL)


def setinformacao():
    url = "https://teste-697ff-default-rtdb.firebaseio.com/.json"

    # Fazendo a requisição GET
    response = requests.get(url)
getinformacao()
    # Verificando se a requisição foi bem-sucedida
if response.status_code == 200:

    print(response.json())

else:
    print(f"Erro na requisição: {response.status_code}")
