from time import sleep


def contador(a, b, c):
    """Faz uma contagem a partir do parâmetro 'a' até o parâmetro 'b' e mostra na tela;
    o parâmtro 'c' é o passo da contagem, ou seja, de quantos em quantos números."""
    print("=" * 40)
    print(f"Contagem de {a} até {b} de {c} em {c}")
    print("=" * 40)
    sleep(3)
    if a < b:
        b += 1
        if c < 0:
            c *= -1
    else:
        b -= 1
        if c > 0:
            c *= -1
    if c == 0:
        c = 1

    for i in range(a, b, c):
        print(i, end=" ", flush=True)
        sleep(.5)
    print("Fim")
    sleep(1)


contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é sua vez de personalizar a contagem!")
contador(int(input("Início: ")), int(input("Fim: ")), int(input("Passo: ")))
