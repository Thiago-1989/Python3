velocidade = int(input('Qual  a velocidade do veículo? \n'))
limite = 80

if velocidade > 80:

    multa = float((velocidade - limite) * 7)

    print('O motorista foi altuado! A velocidade máxima permitida é {}km/h e a multa custará R${:.2f}!'.format(limite, multa))

print('Tenha um bom dia! Dirija com segurança.')
