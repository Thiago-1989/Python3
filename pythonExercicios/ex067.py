# Tabuada com 'while' usando 'break'
cont = 1

while True:
    tab = int(input("\nDigite um valor para ver a tabuada: "))
    if tab < 0:
        break
    print(f"\033[033mA tabuada de {tab} é:\033[m")

    for i in range(0, 10):
        print(f"{tab} x {cont} = {tab * cont}")
        cont += 1
print("Programa TABUADA encerrado!")