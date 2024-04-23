from util import moeda

valor = float(input("Digite um valor: R$"))
print(f"A metade de R${valor} é {moeda.metade(valor)}\n"
      f"O dobro de R${valor} é {moeda.dobro(valor)}\n"
      f"Aumentando 10% de R${valor}, temos {moeda.aumentar(valor, 10)}\n"
      f"Reduzindo 13% de R${valor}, temos {moeda.diminuir(valor, 13)}")
