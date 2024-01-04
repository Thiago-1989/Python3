from random import randint
from time import sleep

cont = 1
numPc = randint(0, 10)  # Sorteia um número entre 0 e 10 conforme parâmetros entre parênteses.

print('-=-' * 20)
print('Sou seu computador e pensei em um número entre 0 e 10. \nTente advinhar qual foi. \n')
print('-=-' * 20)

numUser = int(input('Em qual número eu pensei? \n'))

print('PROCESSANDO...')
sleep(2)

while numPc != numUser:
    cont += 1

    if numPc > numUser:
        print('\nMais... Tente novamente!')
    else:
        print("Menos... Tente novamente")

    numUser = int(input('Em qual número eu pensei? \n'))

    print('PROCESSANDO...')
    sleep(2)

print('\nParabéns! Você acretou! \nEu pensei no número {}.\nVocê fez {} tentativas'.format(numPc, cont))

"""
from random import randint

palpites = 0
acertou = False

numPc = randint(0, 10)  # Sorteia um número entre 0 e 10 conforme parâmetros entre parênteses.

print('-=-' * 20)
print('Sou seu computador e pensei em um número entre 0 e 10. \nTente advinhar qual foi.')
print('-=-' * 20)

while not acertou:
    numUser = int(input('Em qual número eu pensei? \n'))
    palpites += 1

    if numUser == numPc:
        acertou = True
    else:
        if numPc > numUser:
            print('\nMais...  Tente novamente!')
            numUser = int(input('Em qual número eu pensei? \n'))

        else:
            print('\nMenos...  Tente novamente!')
            numUser = int(input('Em qual número eu pensei? \n'))


print('\nParabéns! Você acretou! \nEu pensei no número {}.\nVocê fez {} tentativas'.format(numPc,palpites))
"""