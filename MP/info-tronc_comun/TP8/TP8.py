nom = "p067_triangle.txt"
fichier = open(nom,"rt")
n, t = 100, []
for i in range(n):
    ligne = fichier.readline().rstrip('\n')
    t.append(list(map(int, ligne.split(' '))))
fichier.close

# complexité exponentielle

def somme_max_1(T):
    nm1 = len(T) - 1
    S = {}
    def s(i,j):
        if (i,j) not in S :
            if i == nm1:
                S[(i,j)] = t[i][j]
            else:
                S[(i,j)] = max(s(i+1,j),s(i+1,j+1)) + t[i][j]
        return S[(i,j)]
    m,im,jm = s(0,0),0,0
    for i,j in S.keys:
        if s(i,j) > m :
            m,im,jm = s(i,j),i,j
    return m,im,jm

    

def somme_max_2(T):
    n = len(T)
    S = [[t[i][j] if i == n - 1 else 0 for j in range(i+1) ] for i in range(n)]
    m,im,jm = S[n-1][0],n-1,0
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            S[i][j] = max(S(i+1,j),S(i+1,j+1)) + T[i][j]
            if S[i][j] > m :
                m,im,jm = S[i][j],i,j
    return m,im,jm

def chemin_opt_1(T):
    nm1 = len(T) - 1
    D = {}
    def d(i,j):
        if (i,j) not in D :
            if i == nm1:
                D[(i,j)] = (t[i][j],[t[i][j]])
            else:
                a , cha = d(i+1,j)
                b , chb = d(i+1, j+1) 
                if a > b :
                    D[(i,j)] = (a + t[i][j], [t[i][j]]+cha)
        return D[(i,j)]
    m,im,jm = s(0,0),0,0
    for i,j in S.keys:
        if s(i,j) > m :
            m,im,jm = s(i,j),i,j
    return m,im,jm