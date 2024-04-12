from time import sleep


def maior(* num):
    maior = cont = 0
    print("-=" * 25)
    print("Analizando os valores...")
    sleep(.2)
    print(f"Foram informados {len(num)} valores: ", end="")
    sleep(.2)
    for valor in num:
        print(valor, end=" ")
        sleep(.2)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"\nO maior valor passado foi {maior}")
    print("-=" * 25)


maior(2, 9, 4, 5, 7, 1)
maior(1, 50, 3, 10, 4)
maior(4, 7, 0)
maior(2, 9)
maior(5)
maior()
