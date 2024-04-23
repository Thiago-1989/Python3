def leiaDinheiro(valor=""):
    while True:
        valor = input(valor).strip().replace(",", ".")
        try:
            return float(valor)
        except:
            print("ERRO! ", valor, " é um valor inválido.")
