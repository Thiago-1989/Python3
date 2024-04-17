def voto(ano):
    from datetime import datetime
    from Classe_linha import MyLine
    MyLine().linha(50)
    print(f"{'Sistema de votos':^50}")
    MyLine().linha(50)
    anoAtual = datetime.now().year
    idade = anoAtual - ano
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA."
    elif 16 < idade < 18 or idade >= 65:
        return f"  Com {idade} anos: Voto OPCIONAL."
    else:
        return f"  Com {idade} anos: VOTO OBRIGATÓRIO."


nasc = int(input("Digite o ano de nascimento: "))
print(voto(nasc))
