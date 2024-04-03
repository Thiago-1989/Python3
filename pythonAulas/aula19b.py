brasil = []
estado1 = {"UF": "São Paulo", "Sigla": "SP"}
estado2 = {"UF": "Rio de Janeiro", "Sigla": "RJ"}
brasil.append(estado1)
brasil.append(estado2)
#=====================================================================

brasil = []
estado = {}
for i in range(0, 2):
    estado["UF"] = str(input("UF: "))
    estado["Sigla"] = str(input("Sigla: "))
    brasil.append(estado.copy())
print(brasil)

for estado in brasil:
    for chave, valor in estado.items():
        print(f"{chave}: {valor}")