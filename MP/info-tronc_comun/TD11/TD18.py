def est_clique(L, R):
    for c in R:
        for s in range(len(L)):
            if not c in L[s]:
                return False
            if s in L[c] and not s in R:
                return False
    return True

def Clique_possible(G):
    n = len(G)
    C = []
    S = range(n)
    for s in S:
        if C == [] :
            C.append(s)
        else:
            c = C[0]
            t = False
            if not c in G[s]:
                C = [s]
                t = True
            if not s in G[c]:
                t = True
            if not t:
                C.append(s)
    return C