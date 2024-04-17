def readInt():
    while True:
        print("_" * 30)
        value = input("Digite um número: ")
        print("_" * 30)
        try:
            value = int(value)
            return value
        except:
            print("_" * 30)
            print("\033[031mERRO! Digite um número inteiro válido.\033[m")


num = readInt()
print(f"Você acabou de digitar o número {num}")
