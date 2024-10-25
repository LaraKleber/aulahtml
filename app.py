from flask import (Flask, request, render_template, flash, redirect, url_for) # Importa o flask

app = Flask(__name__) # cria uma instância
app.secret_key = 'segredo'  # Para utilizar flash messages

@app.route("/", methods=( 'GET',)) # Assina uma rota
def index(): # função responsável pela página
    nome = request.args.get('nome') #use seu nome
    return render_template('index.html', nome=nome)

@app.route("/galeria", methods=( 'GET', )) 
def galeria():
    return render_template('galeria.html')

@app.route("/contato", methods=( 'GET', )) 
def contato():
    return render_template('contato.html')

@app.route("/sobre", methods=( 'GET', )) 
def sobre():
    return render_template('sobre.html')

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

@app.route("/tabuada")
@app.route("/tabuada/<int:numero>", methods=['GET'])
def tabuada(numero = None):   

    if 'numero' in request.args: 
       numero = int(request.args.get('numero'))

    return render_template('tabuada.html', numero=numero)

@app.route('/juros', methods=['GET', 'POST'])
def juros():
    if request.method == 'POST':
        try:
            investimento_inicial = float(request.form['investimento_inicial'])
            investimento_mensal = float(request.form['aporte_mensal'])
            juros_ano = float(request.form['juros_ano'])
            tempo_meses = int(request.form['tempo_meses'])

            juros_mensal = juros_ano / 12 / 100
            total = investimento_inicial

            for _ in range(tempo_meses):
                total += investimento_mensal
                total *= (1 + juros_mensal)

            return render_template('juros.html', total=total)
        except ValueError:
            return render_template('juros.html', error="Insira valores válidos.")

    return render_template('juros.html')

@app.route('/imc', methods=['GET', 'POST'])
def imc():
    imc = None
    avaliação = None

    if request.method == 'POST':
        altura = float(request.form['altura'])
        peso = float(request.form['peso'])
        imc = peso / (altura ** 2)

        if imc < 18.5:
            avaliação = 'Você está magro'
        elif imc < 24.9:
            avaliação = 'Você está normal'
        elif imc < 29.9:
            avaliação = 'Você está em Sobrepeso - Grau 1'
        elif imc <39.9:
            avaliação = 'Você está em Obesidade - Grau 2'
        else:
            avaliação = 'Você está em Obesidade Grave - Grau 3'

    return render_template('imc.html', imc=imc, avaliação=avaliação)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        if email == 'aluno@senai.br' and senha == 'senai':
            flash('Login efetuado', 'successo')
            return redirect(url_for('login'))
        else:
            flash('Usuário ou senha incorretos, tente novamente.', 'error')

    return render_template('login.html')


calculos_mensais = []

@app.route('/calculo_energia', methods=['GET', 'POST'])
def calculo_consumo():
    global calculos_mensais

    if request.method == 'POST':
        try:
            nova_medicao = float(request.form['nova_medicao'])
            calculos_mensais.append(nova_medicao)

            
            consumo = [calculos_mensais[i] - calculos_mensais[i - 1] for i in range(1, len(calculos_mensais))]
            valor_kwh = 0.89
            valores = [c * valor_kwh for c in consumo]

            return render_template('consumo.html', medicoes=calculos_mensais, consumo=consumo, valores=valores)

        except ValueError:
            flash("Insira um valor válido.")
            return redirect(url_for('calcular_consumo'))

    return render_template('consumo.html', medicoes=calculos_mensais)
