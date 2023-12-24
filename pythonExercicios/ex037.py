#Leia um número e converta para binário, octal ou hexadecimal, conforme escolha do usuário.

numero = int(input('Digite um número inteiro para convertê-lo: \n').strip())
conversor = str(input('Quer converter para binario, octal ou hexadecimal? (Escreva sem acentos) \n').strip().capitalize())

if conversor == 'Binario':
    print('O número {} em binário é: {}.'.format(numero, bin(numero)[2::]))

elif conversor == 'Octal':
    print('O número {} em octal é: {}.'.format(numero, oct(numero)[2::]))

elif conversor == 'Hexadecimal':
    print('O número {} em hexadecimal é: {}.'.format(numero, hex(numero)[2::]))

else:
    print('Formato inválido! Certifique-se de não usar acentos e tente novamente!')
