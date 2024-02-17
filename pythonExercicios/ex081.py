lista = []
cont = 0
while True:
    lista.append(int(input("Digite um número: ")))
    cont += 1
    while True:
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
        if continuar in "SN":
            break
    if continuar == "N":
        break
print("-=-" * 50)
print(f"\033[032mVocê digitou os seguintes valores: {lista}")
print(f"Ao todo foram digitados {cont} valores.")
print(f"Os valores de forma ordenada  de forma 'decrescente' são: {sorted(lista)[-1::-1]}")
if 5 in lista:
    print(f" O valor 5 está no índice {lista.count(5)} da lista", end=" ")
else:
    print("O valor 5 não foi encontrado na lista.\033[m")