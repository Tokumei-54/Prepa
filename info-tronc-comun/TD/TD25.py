import os as os
fichier = open('/home/eleve/Dokuments/Prepa/info-tronc-comun/TD/metro_paris.txt', 'rt', encoding='utf-8')

Ordre =  376
Taille =  1311 -379 +1
ligne = fichier.readline() # ligne 1 Ã  Ã©liminer

S = []
for i in range(Ordre):
    ligne = fichier.readline().rstrip('\n')
    S.append(ligne[5:])

ligne = fichier.readline() # ligne 378 Ã  Ã©liminer

A = []
for i in range(Taille):
    ligne = fichier.readline().split(' ')
    arc = int(ligne[0]),int(ligne[1]) 
    A.append(( arc , int(float(ligne[2].rstrip('\n')))))

fichier.close()
graphe_metro = (S,A)
print(graphe_metro)

# crÃ©ation de la reprÃ©sentation par liste d'adjacences
def liste_adjacence(G):
    LA = [[] for _ in range(len(G[0]))] # la liste d'adjacence Ã  constituer
    print(len(LA))
    for a in G[1]:
        LA[a[0][0]].append(a[0][1])
    return LA

metro_la = liste_adjacence(graphe_metro)

print(metro_la[:4],'...', metro_la[-4:])

# # stations voisines d'une station donnÃ©e par son nom
# def stations_voisines(g, Noms, station):
#     Ordre = len(Noms)





# print(stations_voisines(metro_la, S, 'OpÃ©ra'))


# # liste des stations d'une ligne de mÃ©tro
# # on suppose que la station en bout de ligne n'appartient qu'Ã  une seule ligne
# def ligne(g, Noms, station):
#     for i, nom in enumerate(Noms):
#         if nom == station:
#             k = i # k est l'indice de la station en bout de ligne
#             break
#     ligne = [station]



#     return ligne
        
# print(ligne(metro_la, S, 'GalliÃ©ni'))
# print(ligne(metro_la, S, 'ChÃ¢teau de Vincennes'))
# print(ligne(metro_la, S, "Mairie d'Issy"))
# print(ligne(metro_la, S, 'Mairie des Lilas'))
# print(ligne(metro_la, S, 'Porte de Clignancourt'))