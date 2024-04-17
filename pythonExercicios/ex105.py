def notas(*n, sit=False):
    """
    -> Função para analizar as notas e situação do aluno.
    - Parâmetro n | notas do aluno (aceita várias).
    - Parâmetros sit= | opcional - indica se deve ou não (True ou False) adicionar a situação do aluno
    - return | Retorna um dicionário com as informações solicitadas
    """
    boletim = {}
    boletim["Total"] = len(n)
    boletim["Maior"] = max(n)
    boletim["Menor"] = min(n)
    boletim["Média"] = sum(n) / len(n)
    if sit:
        if boletim["Média"] < 5:
            boletim["Situação"] = "Ruim"
        elif 5 <= boletim["Média"] < 7:
            boletim["Situação"] = "Razoável"
        else:
            boletim["Situação"] = "Boa"

    return boletim


resp = notas(5.5, 2.5, 1.5, 10, sit=True)
print(resp)
print(help(notas))