n_linhas = int(input('quantas linhas você quer em sua matriz? '))
n_colunas = int(input('quantas colunas você quer em sua matriz? '))
mat = []
for i in range(1, n_linhas + 1):
  linha = []
  for x in range(1, n_colunas + 1):
    numero = int(input(f'Digite um número para a {i}ª linha e {x}ª coluna: '))
    linha.append(numero)
  mat.append(linha)
print(f'Sua Matriz ficou assim: {mat}')