numeros = []
continuar = "S"
while continuar == "S":
    valor = int(input("Digite um número: "))
    if valor not in numeros:
        numeros.append(valor)
        print("Valor adicionado!")
    else:
        print("Esse valor já foi adicionado, digite um valor diferente! ")
    while True:
        continuar = str(input("Deseja continuar [S/N]? ")).upper().strip()[0]
        if continuar in "SN":
            break
        else:
            print("Digite 'S' para sim ou 'N' para não.")
print("Você digitou os numeros: ", end="",)
numeros.sort()
print(numeros)
