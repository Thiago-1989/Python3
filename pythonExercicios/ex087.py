matriz = []
somaPar = somaTerc = 0
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f"Digite um valor para a posição [{i}, {j}]: "))
        linha.append(num)
        if num % 2 == 0:
            somaPar += num
        if j == 2:
            somaTerc += num
    matriz.append(linha)
print("-=-" * 20)
for linha in matriz:
    for item in linha:
         print(f"[{item:^5}]", end=" ")
    print()
print("-=-" * 20)
print(f"A soma dos valores pares é {somaPar}")
print(f"A soma dos valores da da terceira coluna é {somaTerc}")
print(f"O maior valor da segunda linha é {max(matriz[1])}")
