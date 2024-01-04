# 10 termos de uma PA(Progressão aritmética).

print("\033[031mGerador de Prograssão Aritmética\033[m"
      "\n==================================================")
primeiro_termo = int(input("Primeiro termo:\n"))
razao = int(input("Razão:\n"))
cont = 0
print("Os dez primeiros termos da PA solicitada são:\n")

while cont < 10:
    termo = primeiro_termo + cont * razao
    cont += 1

    print(termo, end=" -> ")
print("Fim")
