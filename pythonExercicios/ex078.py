valores = [int(input("Digite um valor: "))]
posicaoMaior = []
posicaoMenor = []

for i in range(1, 5):
    valores.append(int(input("Digite mais um valor: ")))
print(f"Os valores digitados foram: {valores}")
maior = max(valores)
for c in range(0, 5):
    if valores[c] == max(valores):
        posicaoMaior.append(c + 1)
    elif valores[c] == min(valores):
        posicaoMenor.append(c + 1)
print(f"O maior numero digitado foi {max(valores)} na posição ", end=" ")
for valor in posicaoMaior:
    print(valor, end="...")
print(f"\nO menor número digitado foi {min(valores)} na posição ", end=" ")
for num in posicaoMenor:
    print(num, end="...")
print(f"{'FIM':^40}")
