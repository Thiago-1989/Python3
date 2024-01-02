print(" Exercício de Fibonacci ")

n =int( input(" Digite Quantos termos você deseja :"))

a, b = 0, 1

while a < n:
    print(a, end=' -> ')
    a, b = b, a+b
    print(a, b)

print('FIM')
