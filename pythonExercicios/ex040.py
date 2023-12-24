nota1 = float(input('Digite a nota do primeiro semestre: '))
nota2 = float(input('Digite a nota do segundo semestre: '))
media = (nota1 + nota2) / 2

print('Média do aluno: {}'.format(media))
if media > 7:
    print("Status: Aprovado!")

elif media >= 5 and media < 7:
    print('Status: Recuperação!')

else:
    print('Status: Reprovado!')
