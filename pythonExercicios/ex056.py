# Leia nome, idade e sexo de 4 pessoas e diga qual o 'homem' mais velho e quantas mulheres têm menos de 21 anos.

maisVelho = 0
girlMenores = 0
homemMaisVelho = ""
idadeTotal = 0
for i in range(1, 5):
    print("-------{}ª Pessoa-------".format(i))
    name = str(input("Nome: ").strip().capitalize())
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M / F): ").strip().upper())
    idadeTotal = idadeTotal + idade

    if sexo == 'M' and idade > maisVelho:
        homemMaisVelho = name
        maisVelho = idade

    elif sexo == 'F' and idade < 21:
        girlMenores += 1

print("O homem mais velho é {} com {} anos, {} mulheres têm menos de 21 anos e a média de idade "
      "do grupo é {} anos.".format(homemMaisVelho, maisVelho, girlMenores, idadeTotal / 4))
