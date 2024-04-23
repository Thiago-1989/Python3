def dobro(valor=0, formato=False):
    """
        Fumção que retorna o dobro de um valor passado como parâmetro.
        :param valor: Valor base para o calculo
        :param formato: Define se return será formatado para reais
        :return: Retorna o resultado da função
    """
    if formato:
        return real(valor * 2)
    else:
        return valor


def metade(valor=0, formato=False):
    """
        Fumção que retorna a metade de um valor passado como parâmetro.
        :param valor: Valor base para o calculo
        :param formato: Define se return será formatado para reais
        :return: Retorna o resultado da função
    """
    if formato:
        return real(valor / 2)
    else:
        return valor / 2


def aumentar(valor=0, perc=0, formato=False):
    """
        Função que acrescenta percentual a um valor
        :param valor: Valor base do cálculo
        :param perc: Valor percentual a ser acrescentado
        :param formato: Define se return será formatado para reais
        :return: Retorna o resultado da função
    """
    if formato:
        return real(valor + (valor * (perc / 100)))
    else:
        return valor + (valor * (perc / 100))


def diminuir(valor=0, perc=0, formato=False):
    """
        Função que subtrai percentual de um valor
        :param valor: valor base do cálculo
        :param perc: valor percentual a ser subtraído
        :param formato: Define se return será formatado para reais
        :return: retorna o resultado da função
    """
    if formato:
        return real(valor - (valor * (perc / 100)))
    else:
        return valor - (valor * (perc / 100))


def real(valor=0):
    """
        Função que formata valores para moeda reais
        :param valor: Valor a ser formatado
        :return: Valor no formato moeda Real BR
    """
    return f"R${valor:.2f}".replace(".", ",")


def resumo(valor=0, aumento=0, redução=0):
    print(f"{'*' * 40} \n{'RESUMO DO VALOR':^40} \n{'*' * 40}")
    print(f"{'Preço analizado:':<20}{real(valor):>20}"
          f"\n{'Dobro do preço:':<20}{dobro(valor, True):>20}"
          f"\n{'Metade do preço:':<20}{metade(valor, True):>20}"
          f"\n{aumento}{'% de aumento':<18}{aumentar(valor, aumento, True):>20}"
          f"\n{redução}{'% de redução':<18}{diminuir(valor, redução, True):>20}")


def leiaDinheiro(valor=""):
    while True:
        valor = input(valor)
        try:
            if "," in valor:
                valor = valor.replace(",", ".")
            valor = float(valor)
            return valor
        except:
            print(f"ERRO! {valor} é um valor inválido.")
