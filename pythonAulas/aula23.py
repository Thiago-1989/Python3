try:
    a = int(input("Digite o numerador: "))
    b = int(input("Digite o denominador: "))
    r = a / b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que você digitou.")
except ZeroDivisionError:
    print("Não é possivel dividir um número por zero.")
except KeyboardInterrupt:
    print("O usuário preferiu não inserir os dados!")
else:
    print(f"O resultado é {r}")
finally:
    print(f"Volte sempre")
    