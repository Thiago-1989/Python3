# Leia nome e duas notas de alunos e no final mostre media individual
from time import sleep

aluno = []
while True:
    linha = []
    nome = input("Digite o nome do aluno: ").strip().capitalize()
    n1 = eval(input(f"Digite a primeira nota do aluno {nome}: ").strip())
    n2 = eval(input(f"Digite a segunda nota do aluno {nome}: ").strip())
    linha.append(nome)
    linha.append(n1)
    linha.append(n2)
    aluno.append(linha)
    continuar = " "
    while continuar not in "SN":
        continuar = input("Deseja continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        break
print("***" * 10)
print(f'{"Nº":^5}', f'{"NOME":<5}', f'{"MÉDIA":>15}')
print("***" * 10)
for i, item in enumerate(aluno):
    print(f'{i:^4}', f'{aluno[i][0]:<10}', f'{aluno[i][2]:>10}')
while True:
    boletim = int(input("Quer as notas de qual aluno? \n(Para finalizar digite 888): "))
    if boletim <= len(aluno):
        print("-=-" * 10)
        print(f"Notas de {aluno[boletim][0]} são: {aluno[boletim][1]} e {aluno[boletim][2]}")
        print("-=-" * 10)
    if boletim == 888:
        print("Finalinzando...")
        sleep(.2)
        break