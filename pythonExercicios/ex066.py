cont = soma = 0

while True:
    number = int(input("Digite um número ([0] para encerrar): \n"))
    soma += number
    if number == 0:
        break
    cont += 1
print(f"Você digitou {cont} números e a soma entre eles é {soma}")
