frase = input('Digite uma frase: \n').strip().lower()

print('A letra "a" aparece ', frase.count('a'), ' vezes. \nEla aparece primeiro na posição ', frase.find('a') + 1,
      '\nA letra "a" aparece por último na posição ', frase.rfind('a')+1)

