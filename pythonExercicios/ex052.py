""" Leia um número inteiro e diga se é primo ou não.
number = int(input('Numero: '))
if number != 1 and number % 2 != 0 or number == 2:
    if number / 1 == number and number / number == 1 and number % 3 != 0:
        print(number, 'é primo')
    else:
        print("Não é primo")
else:
    print("Não é primo")
"""
# Correção do Profº Guanabara (usando FOR):

number = int(input('Numero: '))
total = 0

for i in range(1, number + 1):
    if number % i == 0:
        total += 1
if total == 2:
    print("\033[034mO número {} é primo.".format(number))
else:
    print("\033[031mO número {} não é primo.".format(number))