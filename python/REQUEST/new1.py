import requests
from bs4 import BeautifulSoup
from flask import Flask, request
lista = list()

"biblioteca flask - usando para trabalhar com web"
app = Flask(__name__)
@app.route('/getinfo', methods=['GET'])

"funçao para coletar informaçao"
def getinfo():
    "pagina que eu vou coletar informaçao"
    url = "https://portal.fmu.br/"
    response = requests.get(url)

    "criando obijeto para trabalhar com html"
    soup = BeautifulSoup(response.text, 'html.parser')

    """    links = soup.find_all('a')

    for link in links:
        print(link.get('href'))"""
    "fazer uma busca no documento hmtl e bustar os testo em <p></P>"
    paragrafos = soup.find_all('p')

    "salvar todos os texto em uma lista"
    for paragrafo in paragrafos:
        lista.append(paragrafo.text) 

    "testando lista em uma variavel"
    tests = str(lista[20])

    "o que vai retona e se paresentado na pagina flask"
    return str(tests)

"pagina flask"
if __name__ == "__main__":
    app.run(debug=True)
