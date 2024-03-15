import requests
from flask import Flask, request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/getinfo', methods=['GET'])
def getinformacao():
    url = "https://portal.fmu.br/"

    response = requests.get(url)

    content = response.content

    site = BeautifulSoup(content, 'html.parser')
    noticia = site.find('div', attrs={'class': "rap-dep"})
    return str(response.content)

if __name__ == "__main__":
    app.run(debug=True)
