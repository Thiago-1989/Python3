# Jogo Par ou Ímpar
from random import randint
cont = 0

print("-=-" * 15)
print("Vamos jogar PAR OU ÍMPAR")
print("-=-" * 15)

while True:
    jogador = input("Digite um número de 0 a 10: \n")
    jogador = int(jogador)

    if 0 < jogador < 10:
        jogador = int(jogador)
        opcao = str(input("Par ou Impar (sem acentos)? \n")).strip().capitalize()
        opcao = opcao[0]
        computador = randint(0, 10)
        soma = computador + jogador
        if opcao == "P":
            if soma % 2 == 0:
                print("-=-" * 15)
                print(f"Você jogou {jogador} e o computador {computador} somando {soma} no  total que é um número PAR. "
                      f"\nVocê venceu!!! Vamos jogar novemente.")
                print("-=-" * 15)

                cont += 1
            else:
                print("-=-" * 15)
                print(f"Você jogou {jogador} e o computador {computador} somando {soma} no total que é um número IMPAR")
                print(f"GAME OVER! \nVocê venceu {cont} vezes")
                break

        elif opcao == "I":
            if soma % 2 != 0:
                print("-=-" * 15)
                print(f"Você jogou {jogador} e o computador {computador} somando {soma}"
                      f" no total que é um número IMPAR. \nVocê venceu!!! Vamos jogar novemente.")
                print("-=-" * 15)

                cont += 1
            else:
                print("-=-" * 15)
                print(f"Você jogou {jogador} e o computador {computador} somando {soma} no total que é um número PAR.")
                print(f"GAME OVER! \nVocê venceu {cont} vezes")
                break
    else:
        print("Dados inválidos!")

