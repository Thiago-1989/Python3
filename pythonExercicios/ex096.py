def linha():
    print("_" * 70)


def area(a, b):
    area = a * b
    linha()
    print(f"{'Controle de terrenos':^70}")
    linha()
    print(f"A área de um terrreno {a}m x {b}m é igual a {area}m²\n")
    print(f'{"* FIM *":*^68}')


l = float(input("Largura(M): "))
c = float(input("Comprimento(M): "))
area(l, c)
