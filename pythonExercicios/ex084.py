cadastro = []
dados = []
maiorPeso = menorPeso = 0
while True:
    dados.append(str(input("Nome: ").strip().capitalize()))
    dados.append(float(input("Peso: ").strip()))
    if len(cadastro) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]
    cadastro.append(dados[:])
    dados.clear()
    while True:
        continuar = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
        if continuar in "SN":
            break
    if continuar in "N":
        break
print("-=-" * 25)
print(f"Ao todo foram cadastradas {len(cadastro)} pessoas. \n{cadastro}")
print(f"O maior peso foi {maiorPeso} kilos. Peso de ", end="")
for pessoa in cadastro:
    if pessoa[1] == maiorPeso:
        print(f'[{pessoa[0]}]', end=" ")
print(f"\nO menor peso foi {menorPeso} kilos. Peso de ", end="")
for pessoa in cadastro:
    if pessoa[1] == menorPeso:
        print(f'[{pessoa[0]}]', end=" ")
print()
