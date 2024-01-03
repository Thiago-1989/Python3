# 10 termos de uma PA(Progressão aritmética).

primeiro_termo = int(input("Digite o primeiro termo da progressão aritmética:\n"))
razao = int(input("Digite a razão da PA:\n"))
cont = 0
print("Os dez primeiros termos da PA solicitada são:\n")

while cont < 10:
    termo = primeiro_termo + cont * razao
    cont += 1

    print(termo, end=" -> ")
print("Acabou")
