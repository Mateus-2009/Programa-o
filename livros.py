import pandas as pd

df = pd.read_csv("tabela_livro.csv")
#print(df.info())

"""df_filtrado = df[df["Ano de Publicação"] == 1993]
print(df_filtrado)
"""

livro = {
    "Título do Livro": "Python para Todos",
    "Autor": "Charles Severance",
    "Categoria": "Programação",
    "Ano de Publicação": 2016,
    "Ativo": True
}
#1 ex
df = df.append(livro, ignore_index=True)

#2 ex
livros_programacao = df[df["Categoria"]== "Programação"]



##

'''class Livro:
    def __init__(self, titulo, autor, categoria, ano, ativo):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.ano = ano
        self.ativo = ativo

livro0 = Livro("Livro 0", "Julio", "Programação",2012, "Sim")
livro1 = Livro("Livro 1", "Julio", "Programação",2012, "Sim")
livro2 = Livro("Livro 2", "Julio", "Programação",2012, "Sim")
lista_de_livros = [livro0, livro1, livro2]

for livro in lista_de_livros:
    print(livro.titulo)'''