""" Leia um número de 0 à 9999 e mostre na tela cada um deles separadamente ex:
Digite um número: 1989
Unidade: 9
Dezena: 8
Centena: 9
Milhare: 1

numero = input('Digite um número: ')
print(numero)
numero = numero.split()
print('Unidade: ', numero[0][3], '\nDezena: ', numero[0][2], '\nCentena: ', numero[0][1], '\nMilhar: ', numero[0][0],)

"""
numero = int(input('Digite um número de 0 à 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(u, d, c, m))