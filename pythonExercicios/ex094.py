cadastro = []
pessoa = {}
somaIdade = 0
while True:
    pessoa["nome"] = str(input("Nome: ")).strip().capitalize()
    pessoa["idade"] = int(input("Idade: "))
    while True:
        pessoa["sexo"] = str(input("Sexo (M/F): ")).strip().upper()[0]
        if pessoa["sexo"] in "MF":
            break
    cadastro.append(pessoa.copy())
    somaIdade += pessoa["idade"]
    pessoa.clear()
    while True:
        continuar = str(input("Deseja continuar (S/N)?")).strip().upper()[0]
        if continuar in "SN":
            break
        else:
            print("ERRO! Digite 'S' ou 'N'.")
    if continuar == "N":
        break
med_idade = somaIdade / len(cadastro)
print("-=-" * 20)
print(f"O grupo tem {len(cadastro)} pessoas.")
print(f"A média de idade é de {med_idade} anos.")
print(f"As mulheres cadastradas foram: ", end="")
for pessoa in cadastro:
    if pessoa["sexo"] == "F":
        print(pessoa["nome"], end=" ")

print(f"\nAs pessoas com idade acima da média são: ")
for i in range(len(cadastro)):
    if cadastro[i]["idade"] >= med_idade:
        for key, value, in cadastro[i].items():
            print(f"{key} = {value}; ", end="")