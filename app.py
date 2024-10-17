from flask import (Flask, request) # Importa o flask

app = Flask(__name__) # cria uma instância

@app.route("/", methods=( 'GET',)) # Assina uma rota
def index(): # função responsável pela página
    nome = request.args.get('nome') #use seu nome
    return f"""<h1>Página inicial</h1>
    <p>Olá {nome}, que nome bonito!</p>"""

@app.route("/galeria", methods=( 'GET', )) 
def galeria():
    return "<h1>Galeria</h1>"

@app.route("/contato", methods=( 'GET', )) 
def contato():
    return "<h1>contato</h1>"

@app.route("/sobre", methods=( 'GET', )) 
def sobre():
    return "<h1>sobre</h1>"

@app.route("/area/<float:largura>/<float:altura>", methods=( 'GET', ))
def area(largura: float, altura: float):
    return f"""<h1> A área
    informada >L={largura} * A={altura}
    => Area={largura*altura}</h1>"""

@app.route("/par_ou_impar/<float:numero>", methods=('GET',))
def par_ou_impar(numero):
  if numero % 2 == 0:
    return f"O número {numero} é par."
  else:
    return f"O número {numero} é ímpar."
  
@app.route("/sobrenome/<string:nome>/<string:sobrenome>", methods=('GET',))
def nomesobrenome(nome: str, sobrenome: str):
  return f"""<h1> sobrenome </h1>
  <p>{sobrenome},{nome}</p>"""

@app.route("/potencia/<float:um>/<float:dois>", methods=( 'GET', ))
def potencia(um: float, dois: float):
    return f"""<h1>{um}^{dois}
     ={um**dois}</h1>"""