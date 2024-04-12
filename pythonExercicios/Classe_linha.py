class MyLine:
    def linha(self):
        print("_" * 70)


def contador(a, b, c):
    print("=" * 40)
    print(f"Contagem de {a} até {b} de {c} em {c}")
    print("=" * 40)
    if a < b:
        b += 1
    else:
        b -= 1
        if c > 0:
            c *= -1
    if c == 0:
        c = 1

    for i in range(a, b, c):
        print(i, end=" ")
    print("Fim")


contador(1, 10, 1)
contador(10, 0, 2)
