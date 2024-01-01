# Fatorial

numero = int(input("Digite um número para obter o fatorial:\n"))
resultado = 1
cont = 1

while cont <= numero:
    resultado *= cont
    cont += 1

print(resultado)
# 1*5, 2 * 5, 10*3, 30*4, 120*5