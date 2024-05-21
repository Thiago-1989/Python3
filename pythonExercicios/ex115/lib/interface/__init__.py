def readInt(msg=""):
    while True:
        try:
            value = int(input(msg))
        except (ValueError, TypeError):
            print("\033[031mERRO! Digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("Usuário não digitou nenhum número.")
            return ""
        else:
            return value


def linha(tam=50):
    return "=" * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    for i in range(1, len(lista) + 1):
        print(f"{i} - \033[36m{lista[i - 1]}\033[m")
    print(linha())
    opcao = readInt("Sua opção: ")
    return opcao

"""

    print("_" * 50)
    print(f"{'MENU PRINCIPAL':^50}")
    print("_" * 50)
    print(f"1 - \033[36m\033[m")
    print(f"2 - \033[36m\033[m")
    print(f"3 - \033[36m\033[m")
    print("_" * 50)
    while True:
        try:
            opcao = int(input("\033[33mSua opção: "))
        except:
            print("ERRO! Digite um número inteiro válido")
            continue
        if opcao == 0 or opcao > 3:
            print("ERRO! Digite uma opção válido")
        if 0 < opcao < 4:
            break

        if opcao == 3:  # Sair
            print("_" * 50)
            print(f"{'OPÇÃO 3':^50}")
            print("_" * 50)
            return "Saindo do sistema...Até logo!"

        if opcao == 2:  # Cadastrar pessoa
            return novo()
        if opcao == 1:  # Ver pessoas cadastradas
            return mostra()

print(menu())  

"""