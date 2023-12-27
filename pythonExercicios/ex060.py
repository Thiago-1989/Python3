# Fatorial

numero = int(input("Digite um número para obter o fatorial:\n"))
resultado=1
cont=1

while cont <= numero:
    resultado *= cont
    cont += 1

print(resultado)
