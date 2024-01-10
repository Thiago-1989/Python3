# CAIXA ELETRÔNICO - Simule valor e diga qunatas cedulas de cada valor serão entregues, 50, 20, 10, 1.
print("-=-" * 10)
print("{:-^30}".format("Banco TM"))
print("-=-" * 10)
valor = int(input("VAlor do saque:   R$"))
print("-=-" * 10)
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"{totced} cédulas de R${ced:.2f}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print("-=-" * 10)
print("{:-^30}".format("Volte Sempre!"))
print("-=-" * 10)
