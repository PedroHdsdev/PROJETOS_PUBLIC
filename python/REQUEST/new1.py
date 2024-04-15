import requests
from bs4 import BeautifulSoup
from flask import Flask, request
lista = list()
app = Flask(__name__)


@app.route('/getinfo', methods=['GET'])
def getinfo():
    url = "https://portal.fmu.br/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    """    links = soup.find_all('a')

    for link in links:
        print(link.get('href'))"""

    paragrafos = soup.find_all('p')

    for paragrafo in paragrafos:
        lista.append(paragrafo.text) 

    tests = str(lista[20])

    return str(tests)

print(lista)
if __name__ == "__main__":
    app.run(debug=True)
