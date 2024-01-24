print("=" * 50)
titulo = "Lista de preços"
print(f'{"Listagem de preços":^50}')
print("=" * 50)
listagem = ("Lápis", 1.50, "Borracha", 1.25, "Caderno", 25.00, "Caneta", 2.50, "Mochila", 120.00)
for pos in range(0, len(listagem)):
      if pos % 2 == 0:
            print(f"{listagem[pos]:.<40}", end="")
      else:
            print(f"R${listagem[pos]:>7.2f}")
