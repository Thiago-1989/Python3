lista = []

for i in range(5):
    num = int(input("Digite um valor: "))

    if not lista:
        lista.append(num)
    else:
        for c in range(len(lista)):
            if num < lista[c]:
                lista.insert(c, num)
                break
        else:
            lista.append(num)
print(lista)
