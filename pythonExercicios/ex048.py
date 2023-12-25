# Some de números ímpares divisíveis por 3 no intervalo de 1 e 500

soma = 0
cont = 0
for c in range(1, 501, 2):

    if c % 3 == 0:
        soma += c
        cont += 1

print("A soma de todos os {} números solicitados é {}.".format(cont, soma))
