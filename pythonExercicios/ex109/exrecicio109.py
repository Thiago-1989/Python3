from pythonExercicios.ex109 import moeda

valor = float(input("Digite um valor: R$"))
print(f"A metade de {moeda.real(valor)} é {moeda.metade(valor, True)}\n"
      f"O dobro de {moeda.real(valor)} é {moeda.dobro(valor, True)}\n"
      f"Aumentando 10% de {moeda.real(valor)} temos {moeda.aumentar(valor, 10, True)}\n"
      f"Reduzindo 13% de {moeda.real(valor)} temos {moeda.diminuir(valor, 13, True)}")
