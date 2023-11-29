#média do aluno

n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
n3 = float(input('nota 3: '))
n4 = float(input('nota 4: '))
media = (n1 + n2 + n3 + n4) / 4

print('A média do aluno é {:.1f}.'.format(media))
if media >= 5:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')