from metro_paris_liste_adjacence import metro_la, Noms

def coloriage(g):
    n = len(g)
    couleur = [-1 for _ in range(n)]
    for s in range(len(g)) :
        couleur_voisin = []
        for v in g[s]:
            couleur_voisin.append(couleur[v])
        c = 0
        while c in couleur_voisin:
            c += 1
        couleur[s] = c
    return couleur

def coloriage_inv(g):
    n = len(g)
    couleur = [-1 for _ in range(n)]
    for s in range(len(g)-1,-1,-1) :
        couleur_voisin = []
        for v in g[s]:
            couleur_voisin.append(couleur[v])
        c = 0
        while c in couleur_voisin:
            c += 1
        couleur[s] = c
    return couleur

def main():
    col = coloriage(metro_la)
    max_col = max(col)
    print(max_col + 1)
    for i in range(len(col)):
        if col[i] == max_col :
            print(Noms[i],i)
    col = coloriage_inv(metro_la)
    max_col = max(col)
    print(max_col + 1)
    for i in range(len(col)):
        if col[i] == max_col :
            print(Noms[i],i)
    

if __name__ == "__main__":
    main()