sexo = str
print("Qual o seu sexo?")
while "M" != sexo != "F":
    sexo = str(input()).capitalize().strip()
    if sexo == "M":
        print("Sexo masculino.")
    elif sexo == "F":
        print("Sexo feminino.")
    else:
        print("Dados inválidos, digite novamente")