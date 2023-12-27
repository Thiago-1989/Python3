from random import randint
from time import sleep

cont = 0
numPc = randint(0, 10)  # Sorteia um número entre 0 e 10 conforme parâmetros entre parênteses.

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10, tente advinhar qual foi. \n')
print('-=-' * 20)

numUser = int(input('Em qual número eu pensei? \n'))

print('PROCESSANDO...')
sleep(2)

while numPc != numUser:
    cont += 1

    print('Eu pensei no número {} e não no número {}.'.format(numPc, numUser))
    print('\nTente novamente!')

    numUser = int(input('Em qual número eu pensei? \n'))

    print('PROCESSANDO...')
    sleep(2)

print('\nParabéns! Você acretou! \nEu pensei no número {}.\nVocê fez {} tentativas'.format(numPc,cont + 1))
