#Ler numeros inteiros, dizer quantos foram digitados e sua soma até que flag = 998
flag = 0
cont = 0
pivo = 0
while flag != 998:
    flag = int(input("Digite um número: \n"))
    soma = flag + pivo
    pivo = soma
    cont += 1

print("Você digitou {} números, a soma de todos é {}".format(cont - 1, soma - 998))
