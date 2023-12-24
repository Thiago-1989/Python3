# Leia seis números e some os que forem pares

print("Digite seis números e obtenha a soma de todos os númeeros pares.")
soma = 0
for c in range(1, 7):
    num = int(input())
    if num % 2 == 0:
        soma += num

print("A soma dos números pares digitados é {}".format(soma))