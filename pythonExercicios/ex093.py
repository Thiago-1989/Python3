jogador = {}
gols = []
jogador["Nome"] = str(input("Nome do jogador: ")).strip().capitalize()
partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
for c in range(0, partidas):
    gols.append(int(input(f"Quantos gols na partida {c + 1}? ")))
jogador["Gols"] = gols[:]
jogador["Total"] = sum(gols)
print("*" * 30)
print(jogador)
print("*" * 30)
for key, value in jogador.items():
    print(f"O campo {key} tem o valor {value}")
print("*" * 30)
print(f"O jogador {jogador['Nome']} jogou {partidas} partidas.")
for i in range(1, partidas + 1):
    print(f"=> Na partida {i}, fez {jogador['Gols'][i - 1]}")
print(f" * Somando {jogador['Total']} gols no total.")
