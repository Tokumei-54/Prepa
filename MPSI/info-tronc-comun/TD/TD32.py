def graph_vide():
    return {}

def ajoute_sommet(g,s):
    if s not in g : g[s]= set()

def ajoute_arrete(g,s1,s2):
    ajoute_sommet(g,s1)
    ajoute_sommet(g,s2)
    g[s2].add(s1)
    g[s1].add(s2)

def ajoute_arretes(g,s,l):
    ajoute_sommet(g,s)
    for a in l:
        ajoute_sommet(g,a)
        if a not in g[s] : g[s].add(a)
        if s not in g[a] : g[a].add(s)

G = {'a' : set(['e', 'i']), 'e' : set(['b', 'a', 'c', 'd', 'f']), 'i' : set(['b', 'd', 'a']), 'b' : set(['f', 'c', 'e', 'i']), 'c' : set(['h', 'b', 'e', 'g']), 'f' : set(['h', 'b', 'e', 'g']), 'g' : set(['f', 'h', 'c']), 'h' : set(['f', 'c', 'g']), 'd' : set(['e', 'i']) }

def triangles(g):
    l = []
    for a in g.keys():
        for b in g[a]:
            for c in g[b]:
                if a in g[c]: 
                    t = set([a,b,c])
                    if t not in l : l.append(t)
    return l

print(triangles(G))

def matrice_adjacence(g):
    n = len(g)
    M = [[0 for _ in range(n)] for _ in range(n)]
    S = []
    for s in g :
        S.append(s):