# Leia vários números, diga qual a média, o maior, o menor e pergunte se o usuário quer continuar.

num = int(input("Digite um número: \n"))

continuar = "S"
cont = 0
soma = 0
maior = num
menor = num
while continuar == "S":
    cont += 1
    soma += num

    if maior < num:
        maior = num

    elif menor > num:
        menor = num

    continuar = str(input("Quer continuar? [S/N} ")).upper().strip()
    if continuar == "S":
        num = int(input("Digite um número: \n"))


print("A média dos números digitados foi {:.2f}, o maior número foi {:.2f} e o menor {:.2f}.".format(soma / cont, maior, menor))
