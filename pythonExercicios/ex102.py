def factorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número
    :Parâm 'num': Número a ser calculado
    :Parâm 'show': (opcional) Mostra ou não o calculo
    :'return': Retorna o resultado
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f"{c} x ", end="")
            else:
                print(f"{c} = ", end="")
    return f


num = int(input("Calcule o fatorial de: "))
print(factorial(num, show=True))
