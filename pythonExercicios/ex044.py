#Calcule  o valor a ser pago por um produto considerando forma de pagamento, parcelamento, etc.

print('=' * 20, 'Lojas Oliveira', "=" * 20,)
preco = float(input('Digite o valor do produto: R$').strip())

print('\nQual a forma de pagamento? \n' 
      '\n[1] À vista em dinheiro ou cheque (10% de desconto)'
      '\n[2] À vista no cartão (5% de desconto)'
      '\n[3] Parcelado 2x no cartão de crédito'
      '\n[4] Parcelamento à partir de 3x (20% de juros)')

print('=' * 40)

formaPagamento = int(input().strip())

if formaPagamento == 1:
    print('O preço final será R${:.2f}'.format(preco - preco * .1))

elif formaPagamento == 2:
    print('O preço final será R${:.2f}'.format(preco - preco * .05))

elif formaPagamento == 3:
    print('O preço final será R${:.2f} parcelado em 2 vezes de R${:.2f}.'.format(preco, preco / 2))

elif formaPagamento == 4:
    parcelas = int(input('Qual o número de parecelas? \n'))
    precoFinal = preco + preco * .2
    print('O preço final será R${:.2f}, em {} vezes de R${:.2f}.'.format(precoFinal, parcelas, precoFinal / parcelas))

else:
    print('Opção inválida.')