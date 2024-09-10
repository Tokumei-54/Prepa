
#-------------------------------------------------------------------------------
#   Lecture du fichier du mÃ©tro parisien
#-------------------------------------------------------------------------------
import os as os
repertoire_courant = "/home/eleve/Dokuments/Prepa/info-tronc-comun/TD/"
nom_fichier = '/metro_A_star.txt'
fichier = open(repertoire_courant + nom_fichier, 'rt', encoding='utf-8')
Ordre = 376
Taille = 933
ligne = fichier.readline() # ligne 1 Ã  Ã©liminer
Nom = []
for i in range(Ordre):
    ligne = fichier.readline().rstrip('\n')
    Nom.append(ligne[5:])
ligne = fichier.readline() # ligne 378 Ã  Ã©liminer
Coords = []
for i in range(Ordre):
    ligne = fichier.readline().split(' ')
    coords = int(ligne[1]), int(ligne[2])
    Coords.append(coords)
ligne = fichier.readline() # ligne 755 Ã  Ã©liminer
A = []
for i in range(Taille):
    ligne = fichier.readline().split(' ')
    arete = int(ligne[0]), int(ligne[1]), float(ligne[2])
    A.append(arete)
fichier.close()
S = list(range(Ordre))
G = (S,A)
#-------------------------------------------------------------------------------
#   CrÃ©ation de la reprÃ©sentation par liste d'adjacences pondÃ©rÃ©e
#-------------------------------------------------------------------------------
def liste_adjacence(G):
    S, A = G
    return [[(a[1], a[2]) for a in A if a[0] == x] for x in S]
graphe_metro = liste_adjacence(G)

# print(graphe_metro)
from queue import PriorityQueue
import math

def A_star(g,h,s1,s2):

    n = len(g)
    distance = [math.inf] * n
    predecesseur = [-1] * n
    filep = PriorityQueue()

    distance[s1] = 0
    filep.put(h(s1), s1)

    while not filep.empty():
        _, s = filep.get()
        if s == s2:
            return distance , predecesseur
        for v,p in s:
            d = distance[s] + p 
            if d < distance[v]:
                distance[v] = d
                predecesseur[v] = s 
                filep.put(d + h(v), v)
    return distance , predecesseur




def h (s1, s2, v=10, c=25.7):
    return math.sqrt((s1[0] - s2[0])**2 + (s1[1] - s2[1])**2)*c/v

h(Coords[0],Coords[1])

def plus_court_chemin(g, s1, s2):
    distance , predecesseur = A_star(g,h,s1,s2)
    C = []
    def aux (s):
        if s != s1:
            aux(pred[s])
        C.append(s)
    aux(s2)
    return C