def dobra(lst):
    cont = 0
    while cont < len(lst):
        lst[cont] *= 2
        cont += 1

valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)
