# Leia seis números e some os que forem pares

print("Digite seis números e obtenha a soma de todos os números pares.")
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input())
    if num % 2 == 0:
        soma += num
        cont += 1

print("Você informou {} número(s) par(es) cuja soma é {}".format(cont, soma))