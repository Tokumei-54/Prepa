from typing import Iterable
import numpy as np

def comptage(ch :Iterable) -> dict :
    d = {}
    for c in ch :
        if c in d.keys():
            d[c]+=1
        else :
            d[c] = 1

    return d

def eleves(d):
    e = {}
    for a , b in d.items():
        for c in b:
            e[c] = a
    return e 

def classe(d):
    L=[]
    for t in d.items():
        L.append(t)
    L.sort() 
    return L

scrable = {'A':1,'E':1,'I':1,'L':1,'N':1,'O':1,'R':1,'S':1,'T':1,'U':1,'D':2,'G':2,'M':2,'B':3,'C':3,'P':3,'F':4,'H':4,'V':4,'J':8,'Q':8,'K':10,'W':10,'X':10,'Y':10,'Z':10}

def score(ch):
    n = 0
    for c in ch.upper():
        if c in scrable.keys():
            n += scrable[c]
    return n

def derive(P):
    P_prime = {0:0}
    for i,j in P.items:
        if i > 0:
            P_prime[i-1] = i*j
    return P_prime

occurence = comptage

def compare(T1,T2):
    O = occurence(T2)
    for i in T1:
        if i in O.keys():
            O[i] -= 1
            if O[i] <0:
                return False
        else :
            return False
    for _ , j in O.items():
        if j !=0:
            return False
    return True 


def main():
    print(comptage("test"))
    print(classe(eleves({4:("D","M","Du"),2:("p","Dub","Dum")})))
    print(score("test"))

if __name__=="__main__":
    main()