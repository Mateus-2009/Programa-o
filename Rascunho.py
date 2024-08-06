from flask import Flask, render_template

app = Flask(__name__)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Livro')