# Tabuada com FOR

num = int(input('Quer ver a tabuada de qual número? \n'))
if 0 < num < 11:
    print("A tabuada de {} é: ".format(num))
    for c in range(1, 11):

        print('{} x {} = {}'.format(num, c, num * c))
print("Fim")
