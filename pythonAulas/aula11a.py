nome = 'Thiago'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[34m', nome, '\033[m'))

color = {'limpa':'\033[m',
               'azul':'\033[34m',
               'ciano':'\033[36m'
               }
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(color['ciano'], nome, color['limpa']))
