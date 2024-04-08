from datetime import date

previdencia = {}
previdencia["Nome"] = str(input("Nome: ")).strip().capitalize()
nasc = int(input("Ano de Nascimento: "))
idade = date.today().year - nasc
previdencia["Idade"] = idade
previdencia["Ctps"] = int(input("Carteira de trabalho (0 não possui): "))
if previdencia["Ctps"] > 0:
    previdencia["Contratação"] = int(input("Ano de contratação: "))
    previdencia["Salário"] = float(input("Salário: "))
    previdencia["Aposentadoria"] = previdencia["Contratação"] + 35 - nasc
print("-=" * 20)
for key, value in previdencia.items():
    print(f"{key} tem valor {value}")
