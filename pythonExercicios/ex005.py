from math import pow

num = int(input('Digite um número inteiro: '))

print('Você digitou {}, seu antecessor é {} '
       'e seu sucessor é {}.'.format(num, (num - 1), (num + 1)))

print('O número que digitou elevado ao quadrado é {:.0f}'.format(pow(num,2)))