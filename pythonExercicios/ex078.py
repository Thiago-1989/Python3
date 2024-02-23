valores = []
posicaoMaior = []
posicaoMenor = []
for i in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {i}: ")))
print("=-=" * 25, f"\nOs valores digitados foram: {valores}")
for c in range(0, 5):
    if valores[c] == max(valores):
        posicaoMaior.append(c)
    elif valores[c] == min(valores):
        posicaoMenor.append(c)
print(f"O maior valor digitado foi {max(valores)} na posição ", end=" ")
for valor in posicaoMaior:
    print(valor, end="...")
print(f"\nO menor valor digitado foi {min(valores)} na posição ", end=" ")
for num in posicaoMenor:
    print(num, end="...")
print(f"{'FIM':^40}")
