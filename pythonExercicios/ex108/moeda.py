def aumentar(valor=0, perc=0):
    """
        Função que acrescenta percentual a um valor
        :param valor: Valor base do cálculo
        :param perc: Valor percentual a ser acrescentado
        :return: Retorna o resultado da função
    """
    return valor + (valor * (perc / 100))


def diminuir(valor=0, perc=0):
    """
        Função que subtrai percentual de um valor
        :param valor: valor base do cálculo
        :param perc: valor percentual a ser subtraído
        :return: retorna o resultado da função
    """
    return valor - (valor * (perc / 100))


def dobro(valor=0):
    """
        Fumção que retorna o dobro de um valor passado como parâmetro.
        :param valor: Valor base para o calculo
        :return: Retorna o resultado da função
    """
    return valor * 2


def metade(valor=0):
    """
        Fumção que retorna a metade de um valor passado como parâmetro.
        :param valor: Valor base para o calculo
        :param formato: Define se return será formatado para reais
        :return: Retorna o resultado da função
    """
    return valor / 2


def real(valor=0):
    """
        Função que formata valores para moeda reais
        :param valor: Valor a ser formatado
        :return: Valor no formato moeda Real BR
    """
    return f"R${valor:.2f}".replace(".", ",")
