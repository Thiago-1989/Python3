matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Digite um valor para a posição [{i}], [{j}]: "))
        linha.append(num)
    matriz.append(linha)

for linha in matriz:
    print()
    for item in linha:
        print(f"[{item}]", end=" ")
