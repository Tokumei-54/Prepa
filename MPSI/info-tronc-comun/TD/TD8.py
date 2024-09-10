from itertools import permutations

valeur = [500,200,100,50,20,10,5,2,1] # Exercice 1
 # 6 posibilités pour rendre 7€
def rendu_monnaie_glouton(valeurs, montant):
    pieces = [0 for _ in valeurs]
    for i in range(len(valeurs)):
        if montant >= valeurs[i]:
            #print(i, montant)
            nb = montant // valeurs[i]
            montant -= valeurs[i]*nb
            pieces[i] += nb
            #i -= 1
    return pieces

poids1 = [12,11,8,10] #Exercice 2
valeurs1 = [7,4,3,3]

poids2 = [13,11,8,10]
valeurs2 = [7,4,3,3]

def sac_a_dos(poids_e, valeurs_e):
    poids = poids_e[:]
    valeur = valeurs_e[:]
    poids_tot = 0
    valeur_tot = 0
    while poids_tot < 30 and len(valeur)>0:
        v_max = 0
        for i in range(len(valeur)):
            if valeur[i]> valeur[v_max]:
                v_max = i
            if valeur[i] == valeur[v_max] and poids[i] < poids[v_max]:
                v_max = i
        if poids_tot + poids[v_max]<= 30:
            poids_tot += poids[v_max]
            valeur_tot += valeur[v_max]
        valeur.pop(v_max)
        poids.pop(v_max)
    return valeur_tot

échequier = 8 #Exercice 3

def is_legal(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if i != j and (i + board[i] == j + board[j] or i - board[i] == j - board[j]):
                return False
    return True


def queen_configuration(board_size):
    QC = []
    for board in permutations(range(board_size)):
        if is_legal(board):
            QC.append(board)
    return QC


def display_board(board): #[♕][　]
    for rows in range(len(board)):
        row = ""
        for fields in range(len(board)):
            if fields == board[rows] :
                row += '[●]'
            else:
                row += '[ ]'
        print(row)





def main():
    print(rendu_monnaie_glouton(valeur, 264))
    
    print(sac_a_dos(poids1,valeurs1)) 
    #La solution n'est pas optimale le objet 1 et 2 que selectionne la strategie donne une valeure de 11 mais en selectionant les objets 1,3 et 4 on optient 13
    print(sac_a_dos(poids1,valeurs2))
    # La solution est optimale mais il existe une autre solution avec une valeur egale mais plus d'objets
    
    #n = 0
    #for board in permutations(range(échequier)):
    #    n+=1
    #print(n)
    qc = queen_configuration(échequier)
    print(len(qc))
    print(qc[54])
    display_board(qc[54])

if __name__ == '__main__':
    main()