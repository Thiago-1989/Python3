def dobro(num, formato=False):
    """
        Fumção que retorna o dobro de um valor passado como parâmetro.
        :param num: Valor base para o calculo
        :param formato: Define se return será formatado para reais
        :return: Retorna o resultado da função
    """
    if formato:
        return real(num * 2)
    else:
        return num


def metade(num, formato=False):
    """
        Fumção que retorna a metade de um valor passado como parâmetro.
        :param num: Valor base para o calculo
        :param formato: Define se return será formatado para reais
        :return: Retorna o resultado da função
    """
    if formato:
        return real(num / 2)
    else:
        return num / 2


def triplo(num, formato=False):
    """
        Fumção que retorna o triplo de um valor passado como parâmetro.:param format: Define se return será formatado para reais
        :param num: Valor base para o calculo
        :param formato: Define se return será formatado para reais
        :return: Retorna o resultado da função
    """
    if formato:
        return real(num * 3)
    else:
        return num * 3


def aumentar(num, perc, formato=False):
    """
        Função que acrescenta percentual a um valor
        :param num: Valor base do cálculo
        :param perc: Valor percentual a ser acrescentado
        :param formato: Define se return será formatado para reais
        :return: Retorna o resultado da função
    """
    if formato:
        return real(num + (num * (perc / 100)))
    else:
        return num + (num * (perc / 100))


def diminuir(num, perc, formato=False):
    """
        Função que subtrai percentual de um valor
        :param num: valor base do cálculo
        :param perc: valor percentual a ser subtraído
        :param formato: Define se return será formatado para reais
        :return: retorna o resultado da função
    """
    if formato:
        return real(num - (num * (perc / 100)))
    else:
        return num - (num * (perc / 100))


def real(num):
    """
        Função que formata valores para moeda reais
        :param num: Valor a ser formatado
        :return: Valor no formato moeda Real BR
    """
    return f"R${num:.2f}"


def resumo(num, aumento, redução):
    print(f"{'*' * 40} \n{'RESUMO DO VALOR':^50} \n{'*' * 40}")
    print(f"{'Preço analizado:':<20}{real(num):>20}"
          f"\n{'Dobro do preço:':<20}{dobro(num, True):>20}"
          f"\n{'Metade do preço:':<20}{metade(num, True):>20}"
          f"\n{aumento}{'% de aumento':<18}{aumentar(num, aumento, True):>20}"
          f"\n{redução}{'% de redução':<18}{diminuir(num, redução, True):>20}")
