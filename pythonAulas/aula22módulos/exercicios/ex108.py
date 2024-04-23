from util import moeda

valor = float(input("Digite um valor: R$"))
print(f"A metade de {moeda.real(valor)} é {moeda.real(moeda.metade(valor))}\n"
      f"O dobro de {moeda.real(valor)} é {moeda.real(moeda.dobro(valor))}\n"
      f"Aumentando 10% de {moeda.real(valor)}, temos {moeda.real(moeda.aumentar(valor, 10))}\n"
      f"Reduzindo 13% de {moeda.real(valor)}, temos {moeda.real(moeda.diminuir(valor, 13))}")
