a = [2, 9, 5, 3]
b = a # Fazendo isso estamos vinculando a lista b e a. Altereando uma altera-se a outro automaticamente
b[0] = 7
print(a)
print(b)
a = [2, 9, 5, 3]
b = a[:] # Dessa forma não vinculamos uma lista na outra apenas pegamos seus valores
b[0] = 7
print(a)
print(b)