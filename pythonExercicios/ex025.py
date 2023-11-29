nome = input('Escreva seu nome completo: \n').strip()

print('Esse nome contem "Silva"? ', 'SILVA' in nome.upper())

if 'SILVA' in nome.upper():

    print('Seu nome contém "Silva".', )

else:

    print('Seu nome não contém "Silva".')