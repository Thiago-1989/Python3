from math import sqrt

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = int(sqrt(num))

print('Você digitou {}, o dobro de {} é {}, o triplo de {} é {} e a raiz quadrada de {} '
      'é {}.'.format(num, num, dobro, num, triplo, num, raiz))