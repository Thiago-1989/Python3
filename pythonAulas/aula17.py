lista = ["Thiago"] # Criando uma lista com um item
print(lista)
lista.insert(0,"Maxuele") # Adicionando um item no índice 0
print(lista)
lista.append("Rebeca") # Adicionando um item na última posição
lista.append("Valentina")
print(lista)
del lista[2] # Apaga o item no índice passado como parâmetro
print(lista)
lista.pop(2) # Caso não tenha parâmetro apaga o último ítem, ou o índice passado como parâmetro
print(lista)
lista.remove("Maxuele") # Apaga o item especificado como parâmetro, caso o item não exista causa erro (use if)
print(lista)
