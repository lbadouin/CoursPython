from flask import Flask, request
import pandas as pd
import io
app = Flask(__name__)

@app.route('/test', methods=['GET'])
def hello():
    return "Hello !"

@app.route('/bonjour',methods=['GET'])
def bonjour():
    nom = request.args.get('nom')
    prenom = request.args.get('prenom')

    return 'Bonjour {} {}'.format(prenom, nom)

@app.route('/nblines', methods=['POST'])
def nb_lines():
    data = request.data
    # comme un fichier
    lines = len(io.BytesIO(data).readlines())
    return '{} lignes'.format(lines)


if __name__ == "__main__":
    app.run()

