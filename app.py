from flask import Flask, render_template



app = Flask(__name__)


@app.route("/inicio")
def ola():
    lista = ["O Senhor dos Anéis", "Dom Casmurro", "O Alquimista"]
    return render_template(
        "lista.html", titulo="Listagem de Livros - SENAI", lista_de_livros=lista
    )


@app.route("/curriculo")
def curriculo():
    return render_template("curriculo.html")


app.run(debug=True)

