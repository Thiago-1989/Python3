from datetime import date

print("Digite o ano de nascimento de 7 pessoas para saber quantas são maiores de idade")
maiores = 0
for i in range(0, 7):
    nasc = int(input())
    idade = date.today().year - nasc
    if idade >= 18:
        maiores += 1
print("{} pessoas são maiores de idade.".format(maiores))
