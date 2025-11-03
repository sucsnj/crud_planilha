from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)
CAMINHO = 'planilha.xlsx'  # ou .csv, .xlsm

@app.route('/')
def index():
    df = pd.read_excel(CAMINHO)
    return render_template('index.html', tabela=df.to_html(index=True))

if __name__ == '__main__':
    app.run(debug=True)