from piles import *
from collections import deque

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
    p = creer_pile()
    for x in expr[::-1]:
        if isinstance(x, (int,float,complex)):
            empiler(x,p)
        else :
            a = depiler(p)
            b = depiler(p)
            empiler(eval(str(a)+x+str(b)) ,p)
    return p[0]

def eval_suffixe(expr):
    p = creer_pile()
    for x in expr:
        if isinstance(x, (int,float,complex)):
            empiler(x,p)
        else :
            b = depiler(p)
            a = depiler(p)
            empiler(eval(str(a)+x+str(b)) ,p)
    return p[0]
    
#Exercice 3
def creer_file(n=0) :
    return deque([],n)
    
def enfiler(element, file) :
    file.append(element)
    
def defiler(file) :
    if len(file) > 0 :
        return file.popleft()

def file_vide(file) :
    return file == []

def taille(file) :
    return len(file)

#Exercice 4
def creer_file2(n):
    return [creer_pile(),creer_pile()]

def est_vide(file):
    return file == [[],[]]

def taille_file(file):
    return len(file[0]), len(file[1])

def enfiler_file(element, file):
    file[0].append(element)

def defiler(file):
    file[1].append(file[0].pop())





def main():
    print(parenthesage_simple("(test)()"))
    print(eval_prefixe(['*', '-', 5, 7, 3]))
    print(eval_suffixe([5, 7, '-', 3, '*']))

if __name__ == "__main__":
    main()