def leiaDinheiro(valor=""):
    while True:
        valor = input(valor).strip().replace(",", ".")
        if valor == "" or valor.isalpha():
            print("ERRO! ", valor, " é um valor inválido.")
        else:
            return float(valor)
            break

