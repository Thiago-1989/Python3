# Preço com 5% de desconto
valor = float(input('Digite o valor do produto para saber qual o preço com desconto: '))
preco = valor - 0.05 * valor
print('O preço com  desconto é R${:.2f}'.format(preco))