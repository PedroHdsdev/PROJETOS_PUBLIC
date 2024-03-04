
"""from flask import Flask

app = Flask(__name__)

@app.route('/')
 def hello_world():
    return 'Olá, mundo! Esta é uma aplicação web de teste usando Flask.'

if __name__ == '__main__':
    app.run(debug=True)  """

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/dados')
def obter_dados_da_api():

    url ='https://jsonplaceholder.typicode.com/posts/1'
    response = request.get(url)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'erro': 'Não foi possível obter os dados da API'}), 500

if __name__ == '__main__':
    app.run(debug=True)

