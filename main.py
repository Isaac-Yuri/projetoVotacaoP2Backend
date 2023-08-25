from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={ "/*" : {"origins":"https://isaac-yuri.github.io/*"}})

max_votos = 48

@app.route('/votar', methods=['POST'])
def votar():
    global max_votos
    if max_votos > 0:
        data = request.get_json()
        candidato_votado = data.get('candidato_votado')
        with open('votacao.txt', 'a') as arquivo:
            arquivo.write(f'{candidato_votado}\n')
        
        max_votos -= 1
        return f'Voto registrado para {candidato_votado}'
    
    return 'Votação encerrada'

@app.route('/andamento')
def andamento():
    contagem = {"jeander":0, "gabriel":0, "total":0}
    with open('votacao.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for candidado in linhas:
            if 'jeander' in candidado:
                contagem['jeander'] += 1
            else:
                contagem['gabriel'] += 1
    contagem['total'] = contagem['gabriel'] + contagem['jeander']
    return contagem

if __name__ == '__main__':
    app.run(debug=True)
