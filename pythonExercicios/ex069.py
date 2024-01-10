# Leia idade e sexo, perguntando se continua, e diga quantas pessoas são > 18 anos, quantos homens cadastrados e mulheres < 20 anos
maior18 = homens = mulherMenos20 = 0
while True:
    tipo = " "
    sexo = " "
    continuar = " "
    idade = -1
    print("-=-" * 20)
    print("Cadastre uma pessoa.")
    print("-=-" * 20)
    idade = int(input("Idade:   "))
    while sexo not in 'MF':
        sexo = str(input("Sexo [M/F]:  ")).strip().upper()[0]
    print("-=-" * 20)
    while continuar not in 'SN':
        continuar = str(input("Quer continuar [S/N]?   ")).strip().upper()[0]
    if idade >= 18:
        maior18 += 1
    if sexo == "M":
        homens += 1
    elif sexo == "F" and idade <= 20:
        mulherMenos20 += 1
    if continuar == "N":
        break
print(f"{maior18} pessoa(s) são maior(es) de 18 anos, {homens} homem(homens) cadastrados "
      f"e {mulherMenos20} mulher(mulheres) tem 20 anos ou menos.")
