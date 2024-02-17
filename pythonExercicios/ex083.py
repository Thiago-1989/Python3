equacao = str(input("Digite uma expressão: "))
abrePar = 0
fechaPar = 0

if "+" in equacao or "-" in equacao or "*" in equacao or "/" in equacao:
    for char in equacao:
        if char == "(":
            abrePar += 1
        elif char == ")":
            fechaPar += 1
    if abrePar == fechaPar:
        print("A expressão está correta.")
    else:
        print("A expressão está incorreta.")
else:
    print("Não é uma expressão numérica")


