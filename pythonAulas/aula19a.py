pessoas = {"Nome": "Thiago", "Sexo": "M", "Idade": 34}
for key, value in pessoas.items():
    print(f"{key}: {value}")
del pessoas["Sexo"]