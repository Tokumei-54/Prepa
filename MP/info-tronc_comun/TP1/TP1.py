from typing import List , Any 

def recherche_dicho(L : List[Any], x : Any) -> int:
    n = len(L)
    i = 0
    while i < len(L):
        if L[i] == x :
            return i
    return -1

def exp_rap(x: float, n :int) -> float :
    q,r = divmod(n, 2) 
    if r== 0 :
        return x**(2*q)
    else :
        return x**(2*q) * exp_rap(x,r)
    
def tri_insertion(L:List) -> List :
    l = []
    n = len(L)
    for i in range(n):
        l.append(L[i])
        j = i
        while L[i] > l[j - 1] and j >= 0 :
            l[j], l[j - 1] = l[j - 1], l[j]
            j-=1
    return l

def tri_selection(L : List) -> List :
    T = L[:]
    n = len(L)
    for i in range(n):
        k = i 
        for j in range (i + 1,n):
            if T[k] < T[j] :
                k = j
        T[i], T[k] = T[k], T[i]
    return T

def fusion(l1: List, l2: List)-> List:
    L = []
    n1, n2 = len(l1), len(l2)
    i1, i2 = 0, 0
    while i1 < n1 and i2 < n2:
        if l1[i1] <= l2[i2]:
            L.append(l1[i1])
            i1 += 1
        else :
            L.append(l2[i2])
            i2 += 1
    if i1 == n1 :
        L += l2[i2:]
    else :
        L += l1[i1:]
    return L

def tri_fusion(L:List) -> List:
    n = len(L)
    if n < 2 :
        return L
    m = n//2
    return fusion(tri_fusion(L[:m]),tri_fusion(L[m:]))

print(tri_fusion([8,4,5,7,2,9,1,6,3,0]))
