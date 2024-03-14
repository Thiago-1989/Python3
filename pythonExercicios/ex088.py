from random import randint
matriz = []
palpites = int(input("Deseja gerar quantos palpites? "))
print("=-=" * 10)
print(f'{"Mega Sena":^30}')
print("=-=" * 10)

for i in range(palpites):
    linha = []

    for j in range(6):
        num = randint(0, 60)
        while num in linha:
            num = randint(0, 60)
        linha.append(num)
        linha.sort()

    matriz.append(linha)

    print(f"Jogo {i + 1}: {matriz[i]}")
print("=-=" * 10)
