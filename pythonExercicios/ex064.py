#Ler numeros inteiros, dizer quantos foram digitados e sua soma até que flag = 998
flag = 0
cont = 0
pivo = 0
soma = 0
flag = int(input("\033[035mDigite um número: [Para parar digite 998]\033[m \n"))

while flag != 998:
    soma = flag + pivo
    pivo = soma
    cont += 1
    flag = int(input("\033[035mDigite um número: [Para parar digite 998]\033[m \n"))

print("\033[036mVocê digitou {} números, a soma entre eles é {}\033[m".format(cont, soma))
