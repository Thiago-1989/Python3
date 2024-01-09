# Leia idade e sexo, perguntando se continua, e diga quantas pessoas são > 18 anos, quantos homens cadastrados e mulheres < 20 anos
maior18 = 0
homens = 0
mulherMenos20 = 0

while True:

    while True:
        idade = int(input("Idade: \n"))
        tipo = type(idade)


        sexo = input("Sexo [M/F]: \n").strip().capitalize()
        sexo = sexo[0]
        conti = input("Quer continuar [S/N]? \n").strip().capitalize()

        if idade >= 18:
            maior18 += 1
        if sexo == "M":
            homens += 1
        elif sexo == "F" and idade <= 20:
            mulherMenos20 += 1
        if conti == "N":
            break

print(f"{maior18} pessoa(s) são maior(es) de 18 anos, {homens} homem(homens) cadastrados "
      f"e {mulherMenos20} mulher(mulheres) tem 20 anos ou menos.")
