
# Exercícios da Aula do dia 24/07/2024

## Exercício 1: Criar um formulário de cadastro para os Livros, deve conter o campo para o Título do Livro, Autor, Categoria, Ano de Publicação e Ativo. Ao final aplique CSS ao Formulário
### Obs: Utilize os exemplos da documentação do W3School.

## Exercício 2:
### 1 - Realizar o download da tabela de Livros a seguir [Tabela CSV](https://docs.google.com/spreadsheets/d/17qfn_9NfDtZUteh5GjDCw951poi4kNY4rndevxINnfE/edit?usp=sharing)
### 2 - Crie um arquivo Python para ler os dados da Tabela com o Pandas
### 3 - Crie uma Classe Livros com os atributos do cadastro
### 4 - Desenvolva uma função para percorrer a tabela de Livros eles com a Classe Livros e salve cada instancia em uma lista de Livros
### 5 - Percorra a lista de livros e print apenas os 10 primeiros livros, deve printar o nome do atributo e o valor do atributo.

import pandas as pd

df = pd.read_csv("tabela_livros.csv")

print("df")


















import pandas as pd

# Caminho para o arquivo CSV
arquivo_csv = 'dados.csv'

# Lê o arquivo CSV usando o Pandas
dados = pd.read_csv(arquivo_csv)

# Exibe os dados lidos
print("Dados da Tabela:")
print(dados)