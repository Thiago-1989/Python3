# Programa sorteia nome de um aluno para apagar a lousa

from random import choice

aluno1 = input('Nome: ')
aluno2 = input('Nome: ')
aluno3 = input('Nome: ')
aluno4 = input('Nome: ')
lista = [aluno1, aluno2, aluno3, aluno4]

print('O aluno sorteado foi: {}'.format(choice(lista)))

"""
import random

aluno1 = input('Nome: ')
aluno2 = input('Nome: ')
aluno3 = input('Nome: ')
aluno4 = input('Nome: ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.randint(1,4)

if sorteio == 1:
    print('O aluno sorteado foi: {}'.format(lista[0]))
elif sorteio == 2:
    print('O aluno sorteado foi: {}'.format(lista[1]))
elif sorteio == 3:
    print('O aluno sorteado foi: {}'.format(lista[2]))
else:
    print('O aluno sorteado foi: {}'.format(lista[3]))
"""