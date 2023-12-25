# Leia o peso de 5 pessoas para sabem qual tem o maior e menor peso
peso = {}
maiorPeso = 0.0
menorPeso = 0.0
maisPesado = ""
maisLeve = ""
for i in range(0, 5):
    print(i)
    nome = str(input("Digite o nome: ")).strip().capitalize()
    peso[i] = float(input("Digite o peso: "))

    if i == 0:
        maiorPeso = peso[i]
        menorPeso = peso[i]
        maisPesado = nome
        maisLeve = nome

    elif peso[i] > maiorPeso:
        maiorPeso = float(peso[i])
        maisPesado = nome

    elif peso[i] < menorPeso:
        menorPeso = float(peso[i])
        maisLeve = nome

print("\nO maior peso foi o de {}, com {:.1f}Kg e o menor peso foi o de {} "
      "com {:.1f}Kg.".format(maisPesado, maiorPeso, maisLeve, menorPeso))
