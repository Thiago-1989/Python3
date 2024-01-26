valores = [int(input("Digite um valor: "))]
for i in range(1,5):
    valores.append(int(input("Digite mais um valor: ")))
print(f"Os valores digitados foram: ", end="")
for valor in valores:
    print(valor, end=" ")
print(f"\nO maior valor digitado foi {max(valores)} na {valores.index(max(valores)) + 1}ª posição" 
      f" e o menor valor digitado foi {min(valores)} na {valores.index(min(valores)) + 1}ª posição.")