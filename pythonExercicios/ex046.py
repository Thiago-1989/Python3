# Contagem regressiva com pausa de 1 segundo
from time import sleep
import emoji

print("Contagem regressiva!\n")

for c in range(10, -1, -1):
    print(c)
    sleep(.7)

print(emoji.emojize('Bumm! Bumm! Poow! 🎆'))
