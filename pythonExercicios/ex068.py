# Jogo Par ou Ímpar
from random import randint
cont = 0
print("-=-" * 15)
print("Vamos jogar PAR OU ÍMPAR")
print("-=-" * 15)
while True:
    jogador = int(input("Digite um número de 0 a 10: \n"))
    computador = randint(0, 10)
    soma = jogador + computador
    opcao = ' '

    while opcao not in 'PI':
        opcao = str(input("Par ou Impar [P/I]? \n")).strip().capitalize()[0]

    print(f"Você jogou {jogador} e o computador {computador} somando {soma} no  total.")

    if opcao == "P":
        if soma % 2 == 0:
            print("-=-" * 15)
            print("Você venceu!!! Vamos jogar novemente.")
            print("-=-" * 15)
            cont += 1
        else:
            print("-=-" * 15)
            print(f"GAME OVER! \nVocê venceu {cont} vezes")
            break

    elif opcao == "I":
        if soma % 2 != 0:
            print("-=-" * 15)
            print("Você venceu!!! Vamos jogar novemente.")
            print("-=-" * 15)
            cont += 1
        else:
            print("-=-" * 15)
            print(f"GAME OVER! \nVocê venceu {cont} vezes")
            break
