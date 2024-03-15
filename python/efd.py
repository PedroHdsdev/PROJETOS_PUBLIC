from flask import Flask, request

app = Flask(__name__)

url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"


response = requests.get(url)


if response.status_code == 200:
    
   print(response.status_code)

else:
    print(f"Erro na requisição: {response.status_code}")
