# Sequência de FIBONACCI
print("\033[032mSequência de FIBONACCI\033[m"
      "\n\033[031m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m")
a = 0
b = 1
c = 0
n =int( input("\033[032mDigite Quantos termos você deseja ver:\n"))
while n > 0:
    print(a, end=" -> ")
    a = b
    b = b + c
    c = a
    n -= 1
print("Fim")
