a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c)
print(d)
print(sorted(c)) #Sorted organiza a tupla sem alterá-la
print(len(c))
print(f"O número 5 aparece {c.count(5)}")
print("O indice de 8 é", c.index(8))
print(c.index(5, 1)) #Nesse caso mostrará em qual posição o 5 aparece partindo do índice 1. O segundo prametro é o "deslocamento"
# As tuplas em python aceitam dados  de tipos diferentes como o exemplo abaixo:
pessoa = ("Thiago", 34, "M", 62)
print(pessoa)
del(pessoa) #Podemos apagar a tupla dusando 'del'
