# Interctive help
# help()
# print(input().__doc__)

#Docstrings
def contador(a, b, c):
    """
    -> Faz uma contagem a partir do parâmetro 'a' até o parâmetro 'b' e mostra na tela;
    o parâmtro 'c' é o passo da contagem, ou seja, de quantos em quantos números.
    retun: Sem retorno
    """
    cont = a
    while cont <= b:
        print(f"{cont}", end=" ", flush=True)
        cont += c
    print("Fim")


help(contador)