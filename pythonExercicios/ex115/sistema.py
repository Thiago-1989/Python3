from pythonExercicios.ex115.lib.interface import *
from pythonExercicios.ex115.lib.arquivo import *
from time import sleep

arq = "cadastro.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    opcao = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    if opcao == 1:  # Ver pessoas cadastradas
        lerArquivo(arq)
    elif opcao == 2:  # Cadastrar pessoa
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: ")).strip().capitalize()
        idade = readInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif opcao == 3:  # Sair
        sleep(.5)
        cabecalho("Saindo do sistema...Até logo!")
        sleep(.5)
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
    sleep(1)
