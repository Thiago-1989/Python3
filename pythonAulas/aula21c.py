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
    return soma


r1 = soma(5, 3)
r2 = soma(9, 2, 4)
print(f"O resultado da primeira soma foi {r1} e a segunda {r2}")
