frase = 'Curso em Video Python'
print(frase.strip())
print(frase.split())
print(frase[::2])
print(len(frase))
print(frase.count('O'))
print(frase.count('o'))

print(frase.count('o', 0, 13))
print(frase.find('deo'))
print('Curso' in frase)

print(frase.replace('Python', 'Java'))
print(frase, len(frase))
print(frase)
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase2 = '   Aprenda python  '
print(frase2)
print(len(frase2))
print(len(frase2.strip()))
frase2 = frase2.strip()
print(frase, ', ', len(frase))

print(frase.split())
print('-'.join(frase))
