lista = []
listaPar = []
listaImpar = []
while True:
    lista.append(int(input("Digite um número: ")))
    while True:
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
        if continuar in "SN":
            break
    if continuar == "N":
        break
for item in lista:
    if item % 2 == 0:
        listaPar.append(item)
    else:
        listaImpar.append(item)
print("-=-" * 40)
print(f"A lista completa é {lista}")
print(f"A lista de valores pares é {listaPar}")
print(f"A lista de valores ímpares é {listaImpar}")
