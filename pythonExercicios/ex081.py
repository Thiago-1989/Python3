lista = []
while True:
    lista.append(int(input("Digite um número: ")))
    while True:
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
        if continuar in "SN":
            break
    if continuar == "N":
        break
print("-=-" * 50)
print(f"\033[032mVocê digitou os seguintes valores: {lista}")
print(f"Ao todo foram digitados {len(lista)} valores.")
lista.sort(reverse=True)
print(f"Os valores de forma ordenada  de forma 'decrescente' são: {lista}")
if 5 in lista:
    print(f"O valor 5 faz parte da lista")
else:
    print("O valor 5 não foi encontrado na lista.\033[m")