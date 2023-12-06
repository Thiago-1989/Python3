# Esse programa diz se o ano em questão é bissexto ou não.
from datetime import date
ano = int(input('Digite o ano que deseja verificar se é bissexto ou Digite 0 para analizar o ano atual.  \n'))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 & ano % 100 | ano % 400 == 0 :
    print('O ano "{}" é BISSEXTO.'.format(ano))

else:
    print('O ano "{}" NÃO é BISSEXTO.'.format(ano))
