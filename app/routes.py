from flask import Flask, render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    dados = {"nome": "Rafael", "idade": 19, "curso": "PROPROFISSÃO", "profissao": "Engenheiro de Software"}
    return render_template('index.html', dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')