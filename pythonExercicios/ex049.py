# Tabuada com FOR

num = int(input('Digite um número para ver sua tabuada:\n'))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num * c))

