# Estrutura condicional simples
name = input('What`s your name? \n')
name = name.strip()
nameB = name.upper()
if nameB == 'THIAGO':
    print('What a beutiful name!')
print('Good morning, {}!'.format(name))

# Estrutura condicional composta
name = input('What`s your name?')
if nameB == 'THIAGO':
    print('What a beutiful name!')
else:
    print('Your name is so normal. ')
print('Good morning, {}!'.format(name))
