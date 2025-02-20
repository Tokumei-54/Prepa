import numpy as np
import matplotlib.pyplot as plt

def lire(fichier, a, b):
    f = open(fichier)
    lignes = f.readlines()
    f.close()
    data = [ligne.split(',')[a:b+1] for ligne in lignes]
    return np.array(data, dtype=np.double)

def d(A, B):
    return np.linalg.norm(A - B)

def mu(L):
    return np.mean(L, axis=0)

def cluster(L, Classe, j):
    return L[Classe == j]

def variance(L):
    return np.sum([d(x, mu(L))**2 for x in L])

def allocation(L, x):
    return np.argmin(np.array([d(x, y) for y in L]))

def affiche(L, cen, Classe, d1, d2):
    couleurs = ['r', 'g', 'b', 'orange', 'c', 'm', 'y', 'peru']
    plt.scatter(L[:, d1], L[:, d2], c=[couleurs[Classe[i]] for i in range(len(Classe))], marker='.')
    plt.scatter(cen[:, d1], cen[:, d2], c='k', marker='+')
    plt.title('abscisse : ' + str(d1) + ' - ' + 'ordonnée : ' + str(d2))
    plt.show()

def k_Means(I, Classe, C, k, montre=False):
    V, nV = 0, 1e10
    while abs(V - nV) > 1e-7 * nV:
        V, nV = nV, 0
        for i in range(len(I)):
            Classe[i] = allocation(C, I[i])
        for j in range(k):
            bloc = cluster(I, Classe, j)
            if len(bloc) > 0:
                C[j] = mu(bloc)
                nV += variance(bloc)
        if montre:
            print('Variance = ', nV)
            affiche(I, C, Classe, 2, 3)
    return nV

def initialise(L):
    C = I[L]
    Classe = np.zeros(len(I), dtype=np.ubyte)
    Classe[L] = np.arange(len(L))
    return C, Classe

I = lire('/home/eleve/Dokuments/Prepa/MP/info-tronc_comun/TD11/iris.data', 0, 3)
n, k = len(I), 3
var = []
for i in range(30):
    Cinitiaux = np.random.choice(range(n), k, replace=False)
    C, Classe = initialise(Cinitiaux)
    var.append((k_Means(I, Classe, C, k), Cinitiaux))
C, Classe = initialise(min(var, key=lambda r: r[0])[1])
affiche(I, C, Classe, 2, 3)
k_Means(I, Classe, C, k, True)