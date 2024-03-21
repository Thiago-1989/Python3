# Leia nome e duas notas de alunos e no final mostre media individual
from time import sleep

aluno = []
while True:
    ficha = []
    nome = input("Digite o nome do aluno: ").strip().capitalize()
    n1 = float(input(f"Digite a primeira nota do aluno(a) {nome}: ").strip())
    n2 = float(input(f"Digite a segunda nota do aluno(a) {nome}: ").strip())
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    aluno.append(ficha)
    continuar = " "
    while continuar not in "SN":
        continuar = input("Deseja continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        break
print("***" * 10)
print(f'{"Nº":<5}', f'{"NOME":^10}', f'{"MÉDIA":>10}')
print("***" * 10)
for i in range(len(aluno)):
    print(f'{i + 1:^5}', aluno[i][0], f'{aluno[i][2]:>10}')
while True:
    boletim = int(input("Quer as notas de qual aluno? \n(Para finalizar digite 888): "))
    print("-=-" * 10)
    print(f"Notas de {aluno[boletim][0]} são: {aluno[boletim][1]}")
    print("-=-" * 10)
    if boletim == 888:
        print("Finalinzando...")
        sleep(2)
        break