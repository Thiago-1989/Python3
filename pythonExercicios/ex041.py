import datetime

anoAtual = datetime.date.today().year

anoNasc = int(input('Digite o ano de nascimento do atleta: '))

idade = anoAtual - anoNasc

if idade <= 9:
    print('Mirim')

elif idade > 9 or idade <= 14:
    print('Infantil')

elif idade > 14 or idade <= 19:
    print('Junior')

elif idade >= 20:
    print('Senior')

else:
    print('Master')