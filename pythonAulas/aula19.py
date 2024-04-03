filme = {"Título": "Star Wars", "Ano": 1977, "Autor": "George Lucas"}
print(filme)
print(filme.items())
print(filme.values())
print(filme.keys())
for k, v in filme.items():
    print(f"O {k} é {v}")

locadora = {"Star Wars": [{"Ano": 1977, "Autor": "George Lucas"}], "Matrix": [{"Ano": 2000}]}
print(locadora[str(input("Qual filme quer exibir: ")).strip()])