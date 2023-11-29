"""
 Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
 de dias pelos quais ele foi alugado. Calcule o preço a pagar,  sabendo que o carro custa R$60 por dia
 e R$0,15 por Km rodado.
"""

print('Para saber o valor a pagar digite o numero de dias, em seguida, o número de kilômetros rodados.')

dias = int(input('Dias: '))
km = float(input('Km: '))
preco = (dias * 60) + (km * 0.15)

print('O total a pagar é R${:.2f}'.format(preco))