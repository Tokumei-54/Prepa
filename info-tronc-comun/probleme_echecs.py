# 1. a. non il est bloqués 
#    b. non car il faudrait repassé par une case
# 2. 
def indice(C):
    return 8*C[0] + C[1]

# 3.
def coord (i):
    return [i // 8,i % 8]

# 4. 10 17 elle renvoit les deplacements legaux

def casA(n):
    Deplacements = [[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2]]
    L = []
    i, j = coord(n)
    for d in Deplacements:
        u = i + d[0]
        v = j + d[1]
        if u >= 0 and v >= 0 and v < 8 :
            L.append(indice([u,v]))
    return L

# 5. 

ListeCoups = []
ListeCA = []

def init():
    global ListeCoups 
    global ListeCA

    ListeCoups = []
    ListeCA = [casA(i) for i in range(64)]

# 7.

def occupePosition (n):
    global ListeCoups
    ListeCoups.append(n)

    critique = False

    for k in ListeCA(n):
        ListeCA(k).remove(n)
        if ListeCA(k) == []:
            critique = True
    return critique    
    

def liberePosition ():
    global ListeCA
    global ListeCoups
    n = ListeCoups.pop

    for k in ListeCA(n):
        ListeCA(k).append(n)
    
def testePosition (n):
    global ListeCoups
    global ListeCA

    if occupePosition(n) :
        if len(ListeCoups) == 63 :
            return True
        else :
            liberePosition(n)
            return False
    else :
        for k in ListeCA(n):
            if testePosition(k):
                return True
        liberePosition(n)
        return False




init()
print(ListeCA)


