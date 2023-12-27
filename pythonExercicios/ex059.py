# Calculadora
from time import sleep

num1 = 0
num2 = 0
opcao = 0
while opcao != 5:
    print("_______Calculadora_______\n")
    print("Escolha a operação a ser realizada.\n")
    print("__________Menu__________")
    print("[1]Soma \n[2]Multiplicação \n[3]Maior \n[4]Novos números \n[5]Sair ")
    print("\n________________________")
    opcao = int(input("Escolha a opção desejada.\n"))
    if 0 < opcao < 6:
        if opcao != 5 and opcao != 4:
            num1 = int(input("Digite um número: "))
            num2 = int(input("Digite outro número: "))
            if opcao == 1:
                operacao = num1 + num2
                print("A soma entre {} e {} é {}".format(num1, num2, operacao))
                continua = str(input("Deseja continuar [S/N]?")).upper().strip()
                if continua == "N":
                    opcao = 5
            elif opcao == 2:
                operacao = num1 * num2
                print("A mutiplicação entre {} e {} é {}".format(num1, num2, operacao))
                continua = str(input("Deseja continuar [S/N]?")).upper().strip()
                if continua == "N":
                    opcao = 5
            elif opcao == 3:
                if num1 == num2:
                    print("Os dois números são iguais.")
                    continua = str(input("Deseja continuar [S/N]?")).upper().strip()
                    if continua == "N":
                        opcao = 5
                elif num1 > num2:
                    operacao = num1
                    print("O maior número digitado foi {}".format(operacao))
                    continua = str(input("Deseja continuar [S/N]?")).upper().strip()
                    if continua == "N":
                        opcao = 5
                else:
                    operacao = num2
                    print("O maior número digitado foi {}".format(operacao))
                    continua = str(input("Deseja continuar [S/N]?")).upper().strip()
                    if continua == "N":
                        opcao = 5
        elif opcao == 4:
            print("Reiniciando...")
            sleep(2)
        elif opcao == 5:
            print("_____FIM_____")
    else:
        sleep(1)
        print("Opção inválida! Tente novamente.")
        sleep(1)
        print("Reiniciando...")
        sleep(2)