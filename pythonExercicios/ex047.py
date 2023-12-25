# Todos os numeros pares entre 1 e 50.

print("Os números pares entre 1 e 50 são: ")

for c in range(2, 51, 2):
    print(c, end=' ')

"""
'Dessa forma o consumo  de memória é maior

for c in range(2, 51):
    if c % 2 == 0:
        print(c, end=' ')
"""
