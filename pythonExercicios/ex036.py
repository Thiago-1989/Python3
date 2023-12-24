# Financiamento de imóvel sem juros.

valorCasa = float(input('Digite o valor do imóvel: \n'))
salario = float(input('Digite o seu salario: '))
anosQuitar = int(input('Em quantos anos deseja pagar?'))
parcelas = anosQuitar * 12
valorParcela = valorCasa / parcelas

if valorParcela <= salario*0.3:
    print('Financiamento aprovado!')
    print('Valor do imóvel: R${:.2f} \nNúmero de parcelas: {}\nValor da parcela: R${:.2f}'.format(valorCasa, parcelas,
                                                                                                  valorParcela))
elif valorParcela == salario * 0.3:
    print("Financiamento em análize, assim que tivermos uma resposta entraremos em contato.")

else:
    print('Sinto muito mas não foi possível prosseguir com seu financiamento no momento.')
