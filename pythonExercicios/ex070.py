total = maisDeMil = menorPreco = 0
maisBarato = ' '
while True:
    ṕroduto = str(input("Nome do produto: \n"))
    preco = float(input("Digite o preço: \nR$"))
    continuar = ' '
    total += preco
    if total == 1:
        menorPreco = preco
        maisBarato = ṕroduto
    elif preco < menorPreco:
            menorPreco = preco
            maisBarato = ṕroduto
    if preco >= 1000:
        maisDeMil += 1
    while continuar not in 'SN':
        continuar = str(input("Deseja continuar [S/N]")).strip().capitalize()[0]
    if continuar == 'N':
        break
print("{:-^40}".format("FIM"))
print(f"\nO total gasto foi R${total:2.2f}")
