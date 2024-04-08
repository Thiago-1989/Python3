from operator import itemgetter
from random import randint
from time import sleep
players= {}
print("  ** Joguem os dados! **")
print("*" * 30)
for c in range(1,5):
    players[f"player {c}"] = randint(1, 6)
for key, value in players.items():
    print(f"  O {key} tirou {value}")
    sleep(.5)
print("*" * 30)
print("--Ranking dos jogadores--")
print("*" * 30)
ranking = {}
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"  {i + 1}º Lugar: {v[0]} com {v[1]}")
    c += 1
    sleep(.5)

"""
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
"""
