# pile avec les tableaux python
# capacité illimitée

def creer_pile(n=0) :
    "crée une pile vide"
    return []
    
def empiler(element, p) :
    "ajoute l'élément element à la pile p"
    p.append(element)
    
def depiler(p) :
    "renvoie le sommet de la pile p si elle est non vide"
    if len(p) > 0 :
        return p.pop()

def pile_vide(p) :
    "renvoie True si la pile est vide, False sinon"
    return p == []

def taille(p) :
    "renvoie la taille de la pile"
    return len(p)
    
def sommet(p) :
    """renvoie l'élément au sommet de la pile sans le retirer
    si la pile n'est pas vide"""
    if len(p) > 0 :
        return p[-1]