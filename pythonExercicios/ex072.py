number = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
          "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    indice = int(input("Digite um número entre 0 e 20: "))
    continuar = " "
    if 0 <= indice <= 20:
        print(f"Você digitou o número {number[indice]}")
        continuar = str(input("Deseja continuar [S/N]? ")).upper().strip()[0]
        while continuar not in "SN":
            continuar = str(input("Deseja continuar [S/N]? ")).upper().strip()[0]
        if continuar == "N":
            break
print("=" * 40, "\nPrograma encerrado!")
