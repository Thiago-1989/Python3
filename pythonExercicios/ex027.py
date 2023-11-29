nome = str(input('Digite seu nome completo: ')).strip().split()

lastname = nome[len(nome)-1]

print('Nice to meet you! Your first name is {} and last name is {}.'.format(nome[0], nome[len(nome)-1]))
