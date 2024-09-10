
def circuit(g):
    n = len(g)
    c = [-1]*n 
    cir = False
    def aux (s):
        nonlocal cir
        if not cir :
            c[s] = 0
            for v in g[s]:
                if c[v] == 0:
                    cir = True
                elif c[v] == -1:
                    aux(v)
            c[s] = 1
    for s in range(n):
        if c[s] == -1 and not cir :
            aux(s)
    return cir

graph_1 = [
    [1, 2],    # 0
    [3, 4], # 1
    [5, 6],       # 2
    [],       # 3
    [],        # 4
    [],
    []
]

graph_2 = [
    [1],    # 0
    [0, 2], # 1
    [1, 3], # 2
    [2, 1]  # 3
]

print(circuit(graph_1))
print(circuit(graph_2))