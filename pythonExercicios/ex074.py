from random import randint
numeros = (randint(0, 100), randint(0, 100), randint(0, 100),
           randint(0, 100), randint(0, 100))
print("Os valores digitados foram ", end="")
for n in numeros:
    print(n, end=" ")
print(f"\nO maior valor sorteado foi {max(numeros)}")
print(f"O menor valor sorteado foi {min(numeros)}")
"""
print(f"Os valores sorteados foram: {numeros}.")
print(f"O maior valor sorteado foi {sorted(numeros)[-1]}")
print(f"O menor valor sorteado foi {sorted(numeros)[0]}")
"""
