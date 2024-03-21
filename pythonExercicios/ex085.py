matriz = [[], []]

for i in range(1, 8):
    valor = eval(input(f"Digite o {i}º valor: "))
    if valor % 2 == 0:
        matriz[0].append(valor)
    else:
        matriz[1].append(valor)
matriz[0].sort()
matriz[1].sort()
print("-=-" * 20)
print(f"Os valores pares digitdos foram: {matriz[0]}")
print(f"Os valores ímpares digitdos foram: {matriz[1]}")
