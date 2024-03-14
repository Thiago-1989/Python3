# Leia nome e duas notas de alunos e no final mostre media individual
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
for i in range(len(aluno)):
    print(f'{i + 1:^5}', f'{aluno[i][0]:<5}', f'{(aluno[i][1] + aluno[i][2]) / 2:>15}')

boletim = 0
while boletim != 888:
    boletim = int(input("Quer as notas de qual aluno? (\nPara finalizar digite 888): "))
    print(aluno[boletim])
