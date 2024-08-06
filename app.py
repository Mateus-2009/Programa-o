from flask import Flask, render_template, request

app = Flask(__name__)

class Livro:
    def __init__(self, titulo, autor, categoria, ano, editora='Sem Editora'):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.ano = ano
        self.editora = editora

# Lista de livros inicial
livro1 = Livro('1984', 'George Orwell', 'Ficção', 1949)
livro2 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 'Fantasia', 1954)
livro3 = Livro('Dom Casmurro', 'Machado de Assis', 'Romance', 1899)
lista = [livro1, livro2, livro3]

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Livro')

@app.route('/criar', methods=['POST'])
def criar():
    # Captura os dados do formulário
    titulo = request.form['titulo']
    autor = request.form['autor']
    categoria = request.form['categoria']
    ano = request.form['ano']
    editora = request.form['editora']

    # Cria um novo objeto Livro com os dados recebidos
    livro = Livro(titulo, autor, categoria, ano, editora)

    # Adiciona o novo livro à lista de livros
    lista.append(livro)

    # Renderiza a página lista.html com a lista atualizada de livros
    return render_template('lista.html', titulo='Livros', livros=lista)