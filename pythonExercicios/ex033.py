num1 = int(input('Digite um número: '))
num2 = int(input('Digite um segundo número: '))
num3 = int(input('Digite um terceiro número: '))

lista = {num1, num2, num3}
maior = max(lista)
menor = min(lista)

"""
maior = num1

if num2 > num1 & num2 > num3
    maior = num2
if num3 > num1 & num3 > num2
    maior = num3
    
menor = num1

if num2 < num1 & num2 < num3
    menor = num2
if num3 < num1 & num3 < num2
    menor = num3
"""

print('O maior valor digitado foi {} e o menor valor digitado foi {}.'.format(maior, menor))