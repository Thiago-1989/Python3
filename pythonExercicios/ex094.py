cadastro = []
pessoa = {}
somaIdade = 0
while True:
    pessoa["nome"] = str(input("Nome: "))
    pessoa["idade"] = int(input("Idade: "))
    pessoa["sexo"] = str(input("Sexo (M/F): ")).strip().upper()[0]
    cadastro.append(pessoa.copy())
    somaIdade += pessoa["idade"]
    pessoa.clear()
    while True:
        continuar = str(input("Deseja continuar (S/N)?")).strip().upper()[0]
        if continuar in "SN":
            break
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

print(f"\nAs pessoas com idade acima da média são: ", end="")
for pessoa in cadastro:
    if pessoa["idade"] > med_idade:
        print(pessoa)
