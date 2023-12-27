# Fatorial

print("Digite um número para saber o seu fatorial:\n")
fator = 0
i = 2
while i > 1:
    num = int(input("Digite um número para saber o seu fatorial:\n"))
    i = num
    for c in range(num, 1, -1):
        i -= 1
        cont = i * (i - 1)
        fator = cont * (i - 2)

print(fator)
