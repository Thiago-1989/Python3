#Programa solicita ano de nacscimento e informa se está no prazo para alistamento militar

import datetime

nasc = int(input('Informe o ano em que você nasceu?\n'))
anoAtual = datetime.date.today().year

idade = anoAtual - nasc

if idade < 18:
    prazoAlista = 18 - idade
    print('Você deve se alistar em {}, faltam {} anos para você se alistar.'.format(anoAtual + prazoAlista, prazoAlista))

elif idade == 18:
    print('Está na hora de se alistar, dirija-se a junta militar da sua cidade!')

else:
    anosAtraso = idade - 18
    print('Você devia ter se alistado em {}, há {} anos atrás.'.format(anoAtual - anosAtraso, anosAtraso))