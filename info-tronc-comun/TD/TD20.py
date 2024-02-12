from piles import *

#Exercice 1
#1

def parenthesage_simple(mot):
    p = creer_pile()
    for i in mot :
        if i == '(':
            empiler(i,p)
        elif i == ')':
            if not pile_vide(p):
                depiler(p)
            else :
                return False
    return pile_vide(p)

def parenthesage_simple2(mot):
    p = creer_pile()
    t = []
    for i in range(len(mot)) :
        if mot[i] == '(':
            empiler(i,p)
        elif mot[i] == ')':
            if not pile_vide(p):
                t.append((depiler(p),i))
            else :
                return False
    if pile_vide(p):
        return t
    else:
        return False
        
# plusieur piles

#4
    
def parenthesage_simple3(mot):
    g = 0
    for i in mot:
        if g < 0:
            return False
        elif i == '(' :
            g+=1
        elif i == ')':
            g-=1
    return g == 0


#Exercice 2
#1. * - 5 7 3                      5 7 - 3 *
#2. 
def eval_prefixe(expr):
    


def main():
    print(parenthesage_simple("(test)()"))
if __name__ == "__main__":
    main()