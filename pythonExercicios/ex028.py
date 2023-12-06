from random import randint
from time import sleep #
numPc = randint(0, 5) # Sorteia um número entre 0 e 5 conforme parâmetros entre parênteses.

print('-=-' * 20)

print('Vou pensar em um número entre 0 e 5, tente advinhar qual foi. \n')

print('-=-' * 20)

numUser = int(input('Em qual número eu pensei? \n'))

print('PROCESSANDO...')
sleep(3)

if (numUser >= 0) & (numUser <= 5):

    if numPc == numUser:
        print('\nParabéns! Você acretou!')
        print('Eu pensei no número {}.'.format(numPc))

    else:
        print('\nNão foi desta vez!')
        print('Eu pensei no número {} e não no número {}.'.format(numPc, numUser))


else:
    print('Número inválido!')