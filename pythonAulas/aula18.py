# Listas compostas são listas dentro de listas
lista = []
dados = ["João", 21]
lista.append(dados[:])
dados = ["Ana", 23]
lista.append(dados[:])
print(lista)
