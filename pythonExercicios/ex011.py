""""
Calcule a quantidade de tinta necessária para pintar uma parede, sabendo que 1 litro de tinta pinta uma
área de 2m².
"""
altura = float(input('Qual a altura da parede em metros? '))
largura = float(input('Qual o comprimento da parede em metros? '))
area = altura * largura
qtdTinta = area / 2

print('Sua parede tem a dimensão de {}m x {}m, e a area total é {}m²'
      'para pintar essa parede são necessários {} lintros de tinta.'.format(altura, largura, area, qtdTinta))