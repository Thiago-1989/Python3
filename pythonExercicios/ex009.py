# Tabuada

num = int(input('Digite um número para ver sua tabuada. \n'))
i = 1
while i <= 10:
     tabuada = num * i
     print('{} x {} = {}'.format(num, i, tabuada))
     i = i + 1