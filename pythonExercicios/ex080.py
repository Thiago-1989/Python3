lista = []
for i in range(0, 5):
    num = int(input("Digite um valor: "))
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print("Adicionado no final lista")
    else:
        for c in range(len(lista)):
            if num < lista[c]:
                lista.insert(c, num)
                print(f"Adicionado no índice {c} da lista")
                break
print("-=-" * 40)
print("Os valores digitados foram: ", end="")
for valor in lista:
    print(valor, end=" ")
