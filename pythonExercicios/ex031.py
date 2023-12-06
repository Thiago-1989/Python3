# Calculando o preço da viagem

distancia = float(input('Qual a distância a ser percorrida em km? \n'))

print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))

if (distancia > 0) & (distancia < 10):
    print('Não realizamos viagens curtas.')

elif distancia > 10:
    if distancia <= 200:
        preco = distancia * 0.50

    else:
        preco = distancia * 0.45

    print('O preço dessa passagem é R${:.2f}'.format(preco))

else:
    print('Dados inválidos.')

"""
distancia = float(input('Qual a distância a ser percorrida em km? \n'))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço dessa passagem é R${:.2f}'.format(preco))
"""
