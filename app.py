from flask import Flask, request
import pandas as pd
import json


app = Flask(__name__)

filmes_uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv"

notas_uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/ratings.csv"

filmes = pd.read_csv(filmes_uri)

notas = pd.read_csv(notas_uri)

filmesInJson = filmes.to_json()

notasInJson = notas.head().to_json()

todasAsNotasPossiveis = json.dumps(notas["rating"].unique().tolist())

descriçaoNota = notas.describe().to_json()

y = json.loads(descriçaoNota)

@app.route("/")
def index():
    return "oi mundo"

@app.route('/reating', methods=['GET'])
def index2():
  return y["rating"]

@app.route('/description', methods=['GET'])
def description():
  if request.method == 'GET':
    return y



if __name__ == "__main__":
  app.run(debug=True)
