import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/getinfo', methods=['GET'])
def getinformacao():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

    response = requests.get(url)

    return str(response.json())

if __name__ == "__main__":
    app.run(debug=True)
