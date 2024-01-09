nota1 = float(input('Digite a nota do 1º semestre: '))
nota2 = float(input('Digite a nota do 2º semestre: '))
media = (nota1 + nota2) / 2

# Condição composta
if media >= 6:
    print('Sua media foi {}'.format(media))
else:
    print('Sua media foi {}'.format(media))

# Condição simplificada
print('Meus parabéns!' if media >= 6
      else 'Estude mais!'.format(media))
