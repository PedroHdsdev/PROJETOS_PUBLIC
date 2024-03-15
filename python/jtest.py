
from jungle import Jungle
from jungle.http import Response

app = Jungle()

@app.route('/')
def index(request):
    return Response('Olá, mundo! Esta é uma aplicação Jungle.')

if __name__ == '__main__':
    app.run(debug=True)
