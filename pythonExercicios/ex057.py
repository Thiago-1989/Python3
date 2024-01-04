# |Leia o sexo de uma peesoa, só aceite "M" ou "F", caso contrário peça para digitar novamente.

sexo = str(input("Informe seu sexo: \n")).capitalize()[0].strip()
while sexo not in "MF":
    sexo = str(input("Dados inválidos, digite novamente \n")).capitalize()[0].strip()
print("Sexo {} registrado com sucesso!".format(sexo))


"""
sexo = str
print("Informe seu sexo: \n")
while "M" != sexo != "F":
    sexo = str(input()).capitalize()[0].strip()
    if sexo == "M":
        print("Sexo masculino.")
    elif sexo == "F":
        print("Sexo feminino.")
    else:
        print("Dados inválidos, digite novamente")
print("Sexo {} registrado com sucesso!".format(sexo))
"""