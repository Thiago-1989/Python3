# Programa recebe o tamanho de três retas e diz se podem formar um triângulo e que tipo de triângulo.
print('-=-' * 20)
print('Analizador de triângulos')
print('-=-' * 20)

reta1 = float(input('Digite o comprimento da reta 1: '))
reta2 = float(input('Digite o comprimento da reta 2: '))
reta3 = float(input('Digite o comprimento da reta 3: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:

    if reta1 == reta2 == reta3:
        print('Os segmentos apresentados podem formar um triângulo EQUILÁTERO.')

    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Os segmentos apresentados podem formar um  triângulo ISÓSCELES.')

    else:
        print('Os segmentos apresentados podem formar um triângulo ESCALENO.')

else:
    print('\nAs retas informadas NÃO podem formar um triângulo.')
