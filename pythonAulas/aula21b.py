# Escopo global e local
def escopo(a=0):
    n = 5
    print(f"N local vale {n}")

    n += a
    print(f"Agora N local vale {n}")
# Para tratar a variavel como global dentro do escopo local basta explicitar
def escopoGlobal(a=0):
    global n
    n = 9

n = 7
print(f"N global vale {n}")
escopo(n)
escopoGlobal()
print(f"Agora N global vale {n}")
