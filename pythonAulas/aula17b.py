values = []
for i in range(0, 5):
    values.append(int(input("Digite um valor: ")))
for c, v in enumerate(values):
    print(f"O valor {v} está no índice {c}.")
print("Fim da lista")