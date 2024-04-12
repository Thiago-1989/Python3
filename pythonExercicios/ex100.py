from random import randint
from time import sleep


def sorteia(lista):
    print(f"Sorteando 5 valores para a lista: ", end="")
    sleep(2)
    for i in range(0, 5):
        num = randint(0, 10)
        lista.append(num)
        print(num, end=" ")
        sleep(.5)
    print("Pronto!")
    sleep(.5)


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares de {lista}, temos {soma}")


numeros = []
sorteia(numeros)
somaPar(numeros)
