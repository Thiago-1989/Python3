# Fatorial Ex: 5! = 5 * 4 * 3 * 2 * 1 = 120 (Usar "laço while")
from math import factorial

numero = int(input("Digite um número para obter o fatorial:\n"))
cont = 1
resultado = 1
fatorial = factorial(numero)

while cont <= numero:
    print(cont, end="")
    print(" x " if 0 < cont < numero else " = ", end="")

    resultado *= cont
    cont += 1

print(resultado, "\nO fatorial de {} é {}." .format(numero, resultado))
print("O fatorial de {} usando módulo é {}." .format(numero, fatorial))

"""   CORREÇÃO:

numero = int(input("Digite um número para obter o fatorial:\n"))
fator = 1
print("Calculando {}! = ".format(numero))

while numero > 0:
    print("{} ".format(numero), end="")
    print(" x " if numero > 1 else " = ", end="")
    fator *= numero
    numero -= 1
print(fator)

"""
