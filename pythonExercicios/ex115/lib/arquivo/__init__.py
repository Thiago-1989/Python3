from pythonExercicios.ex115.lib.interface import cabecalho


def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
    except:
        print("\033[31mErro ao criar arquivo!\033[m")
    else:
        print(f"Arquivo '{nome}' criado com sucesso!")


def lerArquivo(nome):
    try:
        ler = open(nome, "rt")
    except:
        print("Erro ao tentar ler o arquivo")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        for linha in ler:
            dado = linha.split(";")
            print(f"{dado[0]:<35}{dado[1]:>5} anos")
    finally:
        ler.close()


def cadastrar(arq, nome="Desconhecido", idade=0):
    try:
        arquivo = open(arq, "at")
    except:
        print("Erro na abertura do arquivo")
    else:
        try:
            arquivo.write(f"{nome};{idade}")
        except:
            print("Erro ao escrever os dados.")
        else:
            print(f"Registro de '{nome}' adicionado!")
            arquivo.close()
