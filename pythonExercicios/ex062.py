# 10 termos de uma Progressão Aritmética, perguntando se o usuário deseja solicitar nova PA.

primeiro_termo = int(input("Digite o primeiro termo da progressão aritmética:\n"))
razao = int(input("Digite a razão da PA:\n"))
cont = 0
continuar = 10
while True:
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

print("Programa encerrado.")