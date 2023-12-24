# Some de números ímpares divisíveis por 3 no intervalo de 1 e 500

soma = 0

for c in range(1, 500):

    if c % 3 == 0:
        soma += c

print(soma)
