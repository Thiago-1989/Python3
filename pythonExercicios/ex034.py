# Calculo de aumento salarial
salario = float(input('Qual o seu salário? \n'))
novoSalario = salario

if salario > 0:
    if salario >= 1250.00:
        aumento = 0.10
        novoSalario = salario + salario * aumento

    else:
        aumento = 0.15
        novoSalario = salario + salario * aumento

    print('Seu salário somado ao aumento será R${:.2f}'.format(novoSalario))


else:
    print('Valor inválido!')
