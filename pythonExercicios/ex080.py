lista = []

for i in range(5):
    num = int(input("Digite um valor: "))

    if not lista:
        lista.append(num)
        print("Adicionado na lista")
    else:
        for c in range(len(lista)):
            if num < lista[c]:
                lista.insert(c, num)
                print(f"Adicionado no índice {c} da lista")
                break
        else:
            lista.append(num)
            print(f"Adicionado no final da lista")
print("-=-" * 40)
print("Os valores digitados foram: ", end="")
for valor in lista:
    print(valor, end=" ")
