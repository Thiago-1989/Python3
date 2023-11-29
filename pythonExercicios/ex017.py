# Calcule a hipotenusa de um triângulo retângulo através dos valores dos catetos.
from math import hypot

catOp = float(input('Digite o comprimento do cateto oposto: '))
catAdj = float(input('Digite o comprimento do cateto adjacente: '))

print('A o comprimento da hipotenusa é {:.2f}'.format(hypot(catOp, catAdj)))