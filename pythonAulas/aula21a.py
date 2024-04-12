# Parâmetros opcionais
# Caso o parâmetro não for informado assume o valor 0
def soma(a=0, b=0, c=0, d=0, e=0):
    """
    Faz a soma de até 5 valores
    a = valor 1
    b = valor 2
    ...
    """
    soma = a + b + c + d + e
    print(f"A soma vale {soma}")


soma(5, 3)
