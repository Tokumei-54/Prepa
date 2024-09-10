from random import sample, randint

#Exercice 1
#2. 
# Etape 1 : g = 0, d = 15 m = 7
# Etape 2 : g = 8, d = 15 m = 11
# Etape 3 : g = 8, d = 10 m = 9
# Etape 4 : g = 10, d = 10 m = 10
#3.
#la suite des valeur de g est croisante et d decroisante
#4.
#parce que x < T[m]
#5.
#parce que x > T[m]

#Exercice 2

def recherche_dichotomique(T, x):
    g, d = 0, len(T)-1
    while g <= d :
        m = (g+d)//2
        if x == T[m]:
            return m
        elif x < T[m]:
            d = m-1
        else:
            g = m+1
    return "Non-Trouvé"

def recherche_dichotomique_rec(T, x, g, d):
    if g <= d :
        m = (g+d)//2
        if x == T[m]:
            return m
        elif x < T[m]:
            return recherche_dichotomique_rec(T,x,g,m-1)
        else:
            return recherche_dichotomique_rec(T,x,m+1,d)
    return "Non-Trouvé"

def r_d_r(T,x):
    return recherche_dichotomique_rec(T,x,0,len(T)-1)
    
#5. la suite des 

#Exercice 3

def puissance(x,n):
    if n == 1 :
        return x
    else : 
        return x*puissance(x,n-1)

#2. il faut (n-1) multiplication O(n)
    
#Exercice 4

def puissance_rapide(x,n):
    if n == 1 :
        return x
    elif n%2==0: 
        return puissance(x,n//2)**2
    else:
        return x*puissance(x,n//2)**2

#2.

def main():
    T = sample(range(1, 10**3), 10**2)
    T.sort()
    print(recherche_dichotomique(T,T[54]))
    print(recherche_dichotomique(T,-1))
    print(r_d_r(T,T[54]))
    print(r_d_r(T,-1))

    x = randint(0,10*2)
    n = randint(0,10*1)
    print(x,n)
    print(x**n)
    print(puissance(x,n))
    

if __name__=='__main__':
    main()