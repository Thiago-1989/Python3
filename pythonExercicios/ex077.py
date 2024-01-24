tupla = ("Thiago", "Maxuele", "Alex", "Wellington", "Valentina", "Rebeca")
for palavra in tupla:
    print(f"\nO nome '{palavra}' tem as seguintes vogais: ", end="")
    for letra in palavra:
        if letra.lower() in "aáãâeéêiíoóõôuúü":
            print(letra, end=" ")