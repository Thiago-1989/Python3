name = input('Escreva seu nome completo: \n')

# Aqui mostramos o nome, como foi escrito, no console.
print('Your name is {}'.format(name.strip()))

# Aqui mostramos o nome, tudo em maiúsculo, no console.
print('Your name in capital letter is {}'.format(name.upper()))

# Aqui mostramos o nome, tudo em minúsculo, no console.
print('Your name in lowercase lettter is {}'.format(name.lower()))

# Aqui mostramos no console quantas letras tem na cadeia de string sem incluir os espaços.
print('your name has {} letter on the total'.format(len(name.replace(" ", ""))))

""" 
Agora mostramos no console quantas letras tem o primeiro nome, para isso dividimos a string fomando uma lista
e mostrando o tamanho do conteúdo do primeiro item. 
"""
# print(name.find(' ')) or
name = name.split()
print('Your first name is {} and it´s have {} letters'.format(name[0], len(name[0])))