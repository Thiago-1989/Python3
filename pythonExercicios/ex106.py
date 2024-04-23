def pyHelp():
    while True:
        titulo = "  Simstema de ajuda pyHelp"
        print("\033[30;42m" + "~" * (len(titulo) + 2))
        print(titulo)
        print("~" * (len(titulo) + 2))
        manual = str(input("\033[m" + "Função ou Biblioteca> ")).strip().lower()
        if manual == "exit":
            encerrar = "  Até logo!!!"
            print("\033[30;41m" + "~" * (len(encerrar) + 2))
            print(f"{encerrar}")
            print("~" * (len(encerrar) + 2))
            break
        fraseAces = f"  Acessando o manual do comando '{manual}'"
        print("\033[44m" + "~" * (len(fraseAces) + 2))
        print(fraseAces)
        print("~" * (len(fraseAces) + 2))
        print("\033[30;47m ")
        try:
            return help(manual)
        finally:
            pyHelp()


pyHelp()
