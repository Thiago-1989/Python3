dicio = {}
dicio["Nome"] = str(input("Nome: ")).strip().capitalize()
dicio["Média"] = float(input("Média: "))
if dicio["Média"] >= 7:
    dicio["Situação"] = "Aprovado"
elif dicio["Média"] >= 5:
    dicio["Situação"] = "Recuperação"
else:
    dicio["Situação"] = "Reprovado"
print("-=" * 20)
for key, value in dicio.items():
    print(f"  -{key} é igual a {value}")