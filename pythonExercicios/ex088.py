from random import randint
from time import sleep
matriz = []
palpites = int(input("Deseja gerar quantos palpites? "))
print("=-=" * 12)
print(f'{"Palpites Mega Sena":^30}')
print("=-=" * 12)
for i in range(palpites):
    lista = []
    sleep(.5)
    for j in range(6):
        num = randint(1, 61)
        while num in lista:
            num = randint(1, 61)
        lista.append(num)
        lista.sort()
    matriz.append(lista[:])
    print(f"Jogo {i + 1}: {matriz[i]}")
print("=-=" * 4, "Boa sorte!", "=-=" * 4)
