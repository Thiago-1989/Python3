from random import randint
from time import sleep
players= {}
print("Joguem os dados!!!")
print("*" * 25)
for c in range(1,5):
    players[f"player {c}"] = randint(1, 6)
for key, value in players.items():
    print(f"O {key} tirou {value}")
    sleep(.5)
print("*" * 25)
print("Ranking dos jogadores: ")
print("*" * 25)
c = 1
for i in sorted(players, key=players.get, reverse=True):
    print(f"{c}º Lugar: {i} com {players[i]}")
    c += 1
    sleep(.5)
