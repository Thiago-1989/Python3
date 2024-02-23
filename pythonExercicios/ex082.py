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
for i, v in enumerate(lista):
    if v % 2 == 0:
        listaPar.append(v)
    else:
        listaImpar.append(v)
print("-=" * 30)
print(f"A lista completa é {lista}")
print(f"A lista de valores pares é {listaPar}")
print(f"A lista de valores ímpares é {listaImpar}")
