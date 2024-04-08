from datetime import datetime
previdencia = {}
previdencia["Nome"] = str(input("  Nome: ")).strip().capitalize()
nasc = int(input("  Ano de Nascimento: "))
idade = datetime.now().year - nasc
previdencia["Idade"] = idade
previdencia["Ctps"] = int(input("  Carteira de trabalho (0 não possui): "))
if previdencia["Ctps"] > 0:
    previdencia["Contratação"] = int(input("  Ano de contratação: "))
    previdencia["Salário"] = float(input("  Salário: "))
    previdencia["Aposentadoria"] = previdencia["Contratação"] + 35 - nasc
print("-=" * 25)
for key, value in previdencia.items():
    print(f" - {key} tem valor {value}")
