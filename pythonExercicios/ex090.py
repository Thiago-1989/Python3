dicio = {}
dicio["Nome"] = str(input("Nome: ")).strip().capitalize()
dicio["Média"] = float(input("Média: "))
if dicio["Média"] > 5:
    dicio["Situação"] = "Aprovado"
else:
    dicio["Situação"] = "Reprovado"
for key, value in dicio.items():
    print(f"{key} é igual a {value}")