print("Escreva o peso de cinco pessoas para sabem qual tem o maior e menor peso")
peso = {}
maiorPeso = 0
maisPesado = ""
for i in range(0, 2):
    print(i)
    nome = str(input("Digite o nome: ")).strip().capitalize()
    peso[i] = int(input("Digite o peso: "))

    if peso[i] > maiorPeso:
        maiorPeso = peso[i]
        maisPesado = nome

print("\nO maior peso foi o de {}, com {}Kg.".format(maisPesado, maiorPeso))
