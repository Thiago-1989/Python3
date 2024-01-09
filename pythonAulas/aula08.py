# import math
from math import pow, sqrt

num = int(input('Digite um número: '))
pot = pow(num, 2)
raiz = sqrt(num)

print('Você digitou {} que elevado ao quadrado é {}, e sua raiz quadrada é {}'.format(num, pot, raiz))
