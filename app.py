from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)
CAMINHO = 'planilha.xlsx'  # ou .csv, .xlsm

@app.route('/')
def index():
    df = pd.read_excel(CAMINHO)
    return render_template('index.html', tabela=df.to_html(index=True))

@app.route('/post', methods=['POST'])
def post():
    dados = request.form.to_dict()
    df = pd.read_excel(CAMINHO)
    df.loc[len(df)] = list(dados.values())
    df.to_excel(CAMINHO, index=False)
    return 'Linha adicionada com sucesso! <a href="/">Voltar</a>'

@app.route('/delete', methods=['POST'])
def delete():
    indice = int(request.form['indice'])
    df = pd.read_excel(CAMINHO)
    df = df.drop(indice)
    df.to_excel(CAMINHO, index=False)
    return 'Linha deletada! <a href="/">Voltar</a>'

@app.route('/put', methods=['POST'])
def put():
    indice = int(request.form['indice'])
    novos_dados = request.form.to_dict()
    del novos_dados['indice']
    df = pd.read_excel(CAMINHO)
    df.loc[indice] = list(novos_dados.values())
    df.to_excel(CAMINHO, index=False)
    return 'Linha atualizada! <a href="/">Voltar</a>'

if __name__ == '__main__':
    app.run(debug=True, port=3000)
