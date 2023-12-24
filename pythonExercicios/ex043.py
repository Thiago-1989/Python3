#Calculo de IMC
from math import pow

altura = float(input('Digite sua altura: '))
peso = float(input('Informe seu peso: '))
imc = peso / pow(altura, 2)

if imc < 18.5:
    print('IMC = {}\nVocê está abaixo do peso.'.format(imc))

elif 18.5 <= imc < 25:
    print('IMC = {}\nVocê está com o Peso ideal.'.format(imc))

elif imc >= 25 and imc < 30:
    print('IMC = {}\nVocê está com Sobrepeso.'.format(imc))

elif imc >= 30 and imc < 40:
    print('IMC = {}\nVocê está com Obesidade.'.format(imc))

elif imc >= 40:
    print('IMC = {}\nVocê está com Obesidade mórbida.'.format(imc))