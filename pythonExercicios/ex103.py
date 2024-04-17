from Classe_linha import MyLine


def ficha(nome="Desconhecido", gols=0):
    MyLine().linha()
    return f"O jogador {nome} fez {gols} gol(s) no campeonato."


nome = str(input("Nome do Jogador: "))
gols = str(input("Numero de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == "":
    print(ficha(gols=gols))
else:
    print(ficha(nome, gols))
