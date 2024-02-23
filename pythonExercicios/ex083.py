expressao = str(input("Digite a expressão: "))
abrePar = 0
fechaPar = 0
if "+" in expressao or "-" in expressao or "*" in expressao or "/" in expressao:
    for char in expressao:
        if char == "(":
            abrePar += 1
        if char == ")":
            fechaPar += 1
    if abrePar == fechaPar:
        print("A expressão está correta.")
    else:
        print("A expressão está incorreta.")
else:
    print("Não é uma expressão matemática")
