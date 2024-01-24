tabela = ("Palmeiras", "Grêmio", "Atlético-MG", "Flamengo", "Botafogo", "Red Bull Bragantino", "Fluminense", 
          "Athletico-PR", "Internacional", "Fortaleza", "São Paulo", "Cuiabá", "Corinthians", "Cruzeiro", 
          "Vasco", "Bahia", "Santos", "Goiás", "Coritiba", "América-MG")
print("=-=" * 20)
print(f"Tabela do Campeonato Brasileiro 2023\n{tabela}")
print("=-=" * 20)
print(f"Os cinco primeiros colocados foram: \n{tabela[0:5]}.")
print("=" * 40)
print(f"Os quatro ultimos colocados foram \n{tabela[-4:]}")
print("=" * 40)
print(f"Todos os times em ordem alfabética são: \n{sorted(tabela)}")
print("=" * 40)
print(f"O time da Cuiabá está na {tabela.index('Cuiabá') + 1}ª posição.")
print("=" * 40)
