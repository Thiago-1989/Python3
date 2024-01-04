# 10 termos de uma Progressão Aritmética, perguntando se o usuário deseja solicitar nova PA.

primeiro_termo = int(input("Gerador de PA \n==============================="
                           "\nPrimeiro termo:\n"))
termo = 1
razao = int(input("Razão:\n"))
cont = 0
continuar = 10
while termo > 0:
    print("Os termos da PA são:\n")
    i = 0
    while i < continuar:
        termo = primeiro_termo + cont * razao
        print(termo, end=" -> ")
        i += 1
        cont += 1

    continuar = int(input("\nQuer ver mais quantos termos? (Digite 0 para encerrar)\n"))
    if continuar == 0:
        break

print("Programa encerrado com {} termos exibidos.".format(cont))