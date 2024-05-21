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

def readFloat(msg=""):
    while True:
        try:
            value = input(msg).strip().replace(",", ".")
            value = float(value)
            return value
        except (ValueError, TypeError):
            print("\033[031mERRO! Digite um número real válido.\033[m")
        except (KeyboardInterrupt):
            print("Usuário não digitou nenhum número.")
            return ""


real = readFloat("Digite um número real: ")
numInt = readInt("Digite um número inteiro: ")
print(f"Você acabou de digitar o número real {real} e o inteiro {numInt}")
