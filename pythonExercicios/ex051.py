# 10 termos de uma PA(Progressão aritmética).

primeiro_termo = int(input("Digite o primeiro termo da progressão aritmética:\n"))
razao = int(input("Digite a razão da PA:\n"))

print("Os dez primeiros termos da PA solicitada são:")
for i in range(10):
    termo = primeiro_termo + i * razao
    print(termo, end=" -> ")
print("Acabou")