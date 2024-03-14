lista = [[],[]]

for i in range(1, 8):
    num = eval(input(f"Digite o {i}º valor: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()

print(f"Os valores pares digitdos foram {lista[0]}")
print(f"Os valores ímpares digitdos foram {lista[1]}")
