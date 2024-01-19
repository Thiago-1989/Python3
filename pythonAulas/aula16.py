# Tuplas

lanche = ("hambúrguer", "suco", "pizza", "pudim")
print("\033[033m",lanche[1])
print(lanche[1:3])
print(lanche[-1])
print(lanche[:2])
print(lanche[-2])
print(lanche[-3:], "\033[m")

for comida in lanche:
    print(f"\033[035mVou comer {comida}.")

for i in range(0, len(lanche)):
    print(f"\033[032mVou comer {lanche[i]}, posição {i}\033[m")

for posicao, comida in enumerate(lanche):
    print(f"\033[031mVou comer {comida}, posição {posicao}\033[m" )

print(sorted(lanche))