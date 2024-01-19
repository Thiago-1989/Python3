name = "Thiago"
age = 34
pay = 5200.3

# Python 2
print("O %s tem %d anos." %(name, age))
# Python 3
print("O {} tem {} anos.".format(name, age))
# Python 3.6+
print(f"O {name:-^20} tem {age} anos e ganha RS{pay:.2f}.")
