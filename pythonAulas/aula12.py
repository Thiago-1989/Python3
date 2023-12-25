name = str(input('Qual é o seu nome? \n'))
name = name.strip().capitalize()
print(name)
if name == 'Thiago':
    print('Que nome bonito!')

elif name == 'Pedro' or name == 'Maria' or name == 'Paulo':
    print('Seu nome é bem popular no Brasil.')

elif name in 'Ana Luisa Juliana Clara':
    print('Belo nome feminino!')

else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia, {}!'.format(name))
