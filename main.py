from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Listas de dados em memória
tecnicos = []
safras = []
pragas = []
fazendas = []
talhoes = [{"nome":"TH 01"}, {"nome":"TH 02"}, {"nome: TH 03"}]
armadilhas = [{"nome":"Arm 01"}, {"nome":"Arm 02"}, {"nome":"Arm 03"}]
apontamentos = []

# Rota para a página de listagem de técnicos
@app.route('/tecnicos')
def tecnicos_list():
  return render_template('tecnicos/index.html', tecnicos=tecnicos)


# Rota para a página de cadastro de pessoas
@app.route('/tecnicos/cadastrar', methods=['GET', 'POST'])
def tecnicos_cad():
  if request.method == 'POST':
    nome = request.form['nome']
    idade = request.form['idade']
    tecnicos.append({'nome': nome, 'idade': idade})
  return render_template('tecnicos/form.html')


# Rota para a página de lista de safras
@app.route('/safras')
def safras_list():
  return render_template('safras/index.html', safras=safras)


# Rota para a página de cadastro de safras
@app.route('/safras/cadastrar', methods=['GET', 'POST'])
def safras_cad():
  if request.method == 'POST':
    nome = request.form['nome']
    safras.append({'nome': nome})
  return render_template('safras/form.html')


# Rota para a página de lista de pragas
@app.route('/pragas')
def pragas_list():
  return render_template('pragas/index.html', pragas=pragas)


# Rota para a página de cadastro de pragas
@app.route('/pragas/cadastrar', methods=['GET', 'POST'])
def pragas_cad():
  if request.method == 'POST':
    nome = request.form['nome']
    nome_cient = request.form['nome_cientifico']
    pragas.append({'nome': nome, 'nome_cientifico': nome_cient})
  return render_template('pragas/form.html')


# Rota para a página de lista de fazendas
@app.route('/fazendas')
def fazendas_list():
  return render_template('fazendas/index.html', fazendas=fazendas)

# Rota para a página de cadastro de fazendas
@app.route('/fazendas/cadastrar', methods=['GET', 'POST'])
def fazendas_cad():
  if request.method == 'POST':
    nome = request.form['nome']
    area = request.form['area']
    endereco = request.form['endereco']
    contato = request.form['contato']
    dono = request.form['dono']
    fazendas.append({'nome':nome,
                     'area':area,
                     'endereco':endereco,
                     'contato':contato,
                     'dono':dono})
  return render_template('fazendas/form.html')


# Rota para a página de lista de apontamentos
@app.route('/apontamentos')
def apontamentos_list():
  return render_template('apontamentos/index.html', apontamentos=apontamentos)


@app.route('/apontamentos/cadastrar', methods=['GET', 'POST'])
def apontamentos_cad():
  if request.method == 'POST':   
    safra = request.form['safra']
    talhao = request.form['talhao']
    armadilha = request.form['armadilha']
    praga = request.form['praga']
    qtd = request.form['qtd']
    dt = request.form['dt']
    apontamentos.append(
      {
        "safra": safra,
        "talhao": talhao,
        "armadilha": armadilha,
        "praga": praga,
        "qtd": qtd,
        "dt": dt
      }
    )
  return render_template('apontamentos/form.html', safras=safras, talhoes=talhoes, pragas=pragas, armadilhas=armadilhas)


# Rota para a página inicial do app
@app.route('/')
def index():
  return render_template('app/index.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
