"""
Digite um valor em reais para saber quantos dólares é possivel comprar.
Considerando a cotação do dólar em R$4,86 (15/11/23)
"""
reais = float(input('Digite o valor que você tem em R$: '))
dolar = reais / 4.86

print('Com {} reais é possível comprar {:.2f} dólares.'.format(reais, dolar))