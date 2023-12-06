# Programa recebe o tamanho de três retas e diz se podem formar um triângulo.
print('-=-' * 20)
print('Analizador de triângulos')
print('-=-' * 20)

reta1 = float(input('Digite o comprimento da reta 1: '))
reta2 = float(input('Digite o comprimento da reta 2: '))
reta3 = float(input('Digite o comprimento da reta 3: '))

#if ((reta2 - reta3) < reta1 < (reta2 + reta3)) & ((reta1 - reta3) < reta2 < (reta1 + reta3)) & ((reta1 - reta2) < reta3 < (reta1 + reta2)):
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:

    print('\nAs retas informadas podem formar um triângulo.')

else:
    print('\nAs retas informadas NÃo podem formar um triângulo.')

