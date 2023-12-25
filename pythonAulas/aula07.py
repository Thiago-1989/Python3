num1 = int(input('Digite um número: '))
num2 = int(input('digite outro num: '))

soma = num2 + num1
subtracao = num2 - num1
multiplicacao = num2 * num1
divisao = num2 / num1
divisaoInt = num2 // num1
exponenciacao = num2 ** num1
resto = num2 % num1

print('=' * 200)
print('A soma é {}, a substração é {}, o produto é {},'.format(soma, subtracao, multiplicacao), end=' ' )
print('a divisão é {}, a divisão inteira é {},a exponenciação é {} e o resto da divisão é {}'.format(divisao, divisaoInt, exponenciacao, resto))
