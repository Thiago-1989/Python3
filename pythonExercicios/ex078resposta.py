valores = []
maior = []
menor = []
for i in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {i}: ")))
    if i == 0:
        maior = menor = valores[i]
    else:
        if maior < valores[i]:
            maior = valores[i]
        elif menor > valores[i]:
            menor = valores[i]
print("=-=" * 25, f"\nOs valores digitados foram: {valores}")

print(f"O maior valor digitado foi {(maior)} na posição ", end="")
for i, v in enumerate(valores):
    if maior == v:
        print(f"{i}", end="...")
print(f"\nO menor valor digitado foi {menor} na posição ", end="")
for i, v in enumerate(valores):
    if menor == v:
        print(i, end="...")
print(f"\n{'FIM':-^50}")
