# Fatorial Ex: 5! = 5 * 4 * 3 * 2 * 1 = 120

numero = int(input("Digite um número para obter o fatorial:\n"))
cont = 1
resultado = 1

while cont <= numero:
    resultado *= cont
    cont += 1

print(resultado)
