# Leia um número inteiro e diga se é primo ou não.

number = int(input('Numero: '))
if number != 1 and number % 2 != 0 or number == 2:

    if number / 1 == number and number / number == 1 and number % 3 != 0:
        print(number, 'é primo')
    else:
        print("Não é primo")
else:
    print("Não é primo")
