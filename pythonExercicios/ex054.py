# Leia o ano de nascimento de 7 pessoas e diga quantas são maiores e quantas são menores de idade

from datetime import date

print("Digite o ano de nascimento de 7 pessoas para saber quantas são maiores de idade")
maiores = 0
menores = 0
for i in range(0, 7):
    nasc = int(input("Em que ano a {}º pessoa nasceu?\n"))
    idade = date.today().year - nasc
    if idade >= 18:
        maiores += 1
    elif idade < 18:
        menores += 1
print("Das sete pessoas {} são maiores de idade e {} são menores.".format(maiores, menores))
