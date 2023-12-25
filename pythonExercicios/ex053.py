"""Leia uma frase e diga se é um 'palíndromo'.

frase = str(input("Escreva uma palavra ou frase para saber se è um PALÍDROMO:\n").strip().upper())

if frase[0::].replace(" ", "") == frase[::-1].replace(" ", ""):
    print("A frase '{}' é um PALÍNDROMO.".format(frase))
else:
    print("A frase '{}' não é um PALÍNDROMO.".format(frase))"""

frase = str(input("Escreva uma palavra ou frase para saber se è um PALÍDROMO:\n").strip().upper())
palavras = frase.split()
junto = "".join(palavras)
inverso = ""

for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]
if inverso == junto:
    print("Temos um palíndromo.".format(frase.upper()))
else:
    print("Não temos um palíndromo.")
