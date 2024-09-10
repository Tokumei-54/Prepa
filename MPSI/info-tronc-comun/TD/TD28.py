#-------------------------------------------------------------------------------
#   Lecture du fichier du mÃ©tro parisien
#-------------------------------------------------------------------------------
import os as os
repertoire_courant = os.getcwd()
nom_fichier = '/metro_paris.txt'
fichier = open(repertoire_courant + nom_fichier, 'rt', encoding='utf-8')
Ordre = 376
Taille = 933
ligne = fichier.readline() # premiÃ¨re ligne Ã  Ã©liminer
Nom = []
for i in range(Ordre):
    ligne = fichier.readline().rstrip('\n')
    Nom.append(ligne[5:])
ligne = fichier.readline() # ligne 378 Ã  Ã©liminer
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
    return [[ (a[1],a[2]) for a in A if a[0]== x] for x in S]

graphe_metro = liste_adjacence(G)
print('DÃ©but du graphe : ', graphe_metro[:4], '\n')

#-------------------------------------------------------------------------------
#   Algorithme de Dijkstra
#-------------------------------------------------------------------------------
from queue import PriorityQueue

def Dijkstra(g,S):
    n = len(g)
    dist = [1000000] * n
    pavu = [True] * n
    P = [-1] * n # prÃ©dÃ©cesseurs
    F = PriorityQueue()
    F.put((0,S))
    dist[S] = 0
    while not F.empty():
        p, s = F.get()
        if pavu[s]:
            pavu[s] = False
            for v in g[s]:
                    d = v[1] + p
                    if d < dist[v[0]]:
                        dist[v[0]] = d
                        P[v[0]] = s 
                    F.put(dist[v[0]],v[0])
    return dist, P

Dijkstra(graphe_metro,0)
#-------------------------------------------------------------------------------
#   Plus court chemin entre deux sommets (version rÃ©cursive)
#-------------------------------------------------------------------------------
def plus_court_chemin(g, s1, s2):
    pred = Dijkstra(g,s1)[1]
    C = []
    def aux (s):
        if s != s1:
            aux(pred[s])
        C.append(s)
    aux(s2)
    return C



#-------------------------------------------------------------------------------
#   Exemple : du sommet 0 (Abbesses) au sommet 1 (Alexandre Dumas)
#-------------------------------------------------------------------------------
pcc = plus_court_chemin(graphe_metro, 0, 1)
print('-> Plus court chemin en temps : ')
print([Nom[i] for i in pcc[0]])
print('Temps de pacours = ', pcc[1]/60, ' minutes\n')

#-------------------------------------------------------------------------------
#   Exemple : du sommet 12 (Avron) au sommet 362 (Victor Hugo)
#-------------------------------------------------------------------------------
pcc = plus_court_chemin(graphe_metro, 12, 362)
print('-> Plus court chemin en temps : ')
print([Nom[i] for i in pcc[0]])
print('Temps de pacours = ', pcc[1]/60, ' minutes\n')

#-------------------------------------------------------------------------------
#   Poids total d'un chemin
#-------------------------------------------------------------------------------
def poids(g, chemin):
    pass

#-------------------------------------------------------------------------------
#   RÃ©cupÃ©ration du graphe non pondÃ©rÃ© reprÃ©sentÃ© par liste d'adjacences
#-------------------------------------------------------------------------------
from metro_paris_liste_adjacence import metro_la, Noms

#-------------------------------------------------------------------------------
#   BFS avec prÃ©dÃ©cesseurs et distances (2 couleurs suffisent ici)
#-------------------------------------------------------------------------------
from queue import Queue
def bfs(g, s):
    pass

#-------------------------------------------------------------------------------
#   Plus court chemin entre deux sommets au sens de la longueur
#-------------------------------------------------------------------------------
def plus_court_largeur(g,s1,s2):
    pass

#-------------------------------------------------------------------------------
pcc = plus_court_largeur(metro_la, 12, 362)
print('-> Plus court chemin en longueur : ')
print([Noms[i] for i in pcc])
print('poids total = ', poids(graphe_metro, pcc)/60, ' minutes\n')

#-------------------------------------------------------------------------------
#   De crÃ©teil PrÃ©fecture Ã  Pont de SÃ¨vre
#-------------------------------------------------------------------------------
s1, s2 = 89, 253
pcc = plus_court_chemin(graphe_metro, s1, s2)
print('-> Plus court chemin en temps : ')
print([Nom[i] for i in pcc[0]])
print('Temps de pacours = ', pcc[1]/60, ' minutes\n')
pcc = plus_court_largeur(metro_la, s1, s2)
print('-> Plus court chemin en longueur : ')
print([Noms[i] for i in pcc])
print('poids total = ', poids(graphe_metro, pcc)/60, ' minutes')


