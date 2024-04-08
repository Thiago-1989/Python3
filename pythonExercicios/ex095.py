atletas = []
while True:
    jogador = {}
    gols = []
    total = 0
    print("=" * 50)
    jogador["Nome"] = str(input("Nome do jogador: ")).strip().capitalize()
    partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
    jogador["Partidas"] = partidas
    for c in range(0, partidas):
        gols.append(int(input(f"Quantos gols na partida {c + 1}? ")))
        total += gols[c]
    jogador["Gols"] = gols
    jogador["n_gols"] = str(gols)
    jogador["Total"] = total
    atletas.append(jogador.copy())
    jogador.clear()
    while True:
        continuar = str(input("Deseja continuar (S/N)?")).strip().upper()[0]
        if continuar in "SN":
            break
    if continuar == "N":
        break
print("*" * 60)
print(f'{"Cod":<5}{"Nome":<15}{"Partidas":<15}{"Gols":<15}{"Total":<10}')
print("-" * 60)
for c in range(len(atletas)):
    print(f'{c:<5}{atletas[c]["Nome"]:<15}{atletas[c]["Partidas"]:<15}{atletas[c]["n_gols"]:<15}{atletas[c]["Total"]:<10}')
while True:
    cod = int(input("Digite o código do jogador para ver rendimento por partida ou 777 para encerrar: "))
    if 0 <= cod < len(atletas):
        print(f"Rendimento do jogador {atletas[cod]['Nome']}")
        for i in range(atletas[cod]["Partidas"]):
            print(f"No jogo {i + 1} fez {atletas[cod]['Gols'][i]} gol(s)")
    elif cod == 777:
        break
    else:
        print("Digite um número válido!")
print("Programa encerrado!")
