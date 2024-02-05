from math import floor
from random import randint

#Exercice 1
def fusion(t1,t2): #1
    T=[]
    i1 = 0
    i2 = 0
    while i1 < len(t1) and i2 < len(t2):
        if t1[i1]<= t2[i2]:
            T.append(t1[i1])
            i1+=1
        else:
            T.append(t2[i2])
            i2+=1
    T+=t1[i1:]+t2[i2:]
    return T

def fusion_2(t1,t2): #2
    T=[]
    t = t1[:]+t2[::-1]
    i = 0
    j = len(t)-1
    while i <= j :
        if t[i]<= t[j]:
            T.append(t[i])
            i+=1
        else:
            T.append(t[j])
            j-=1
    return T

def tri_fusion(T):
    if len(T)<=1:
        return T
    m = floor(len(T)/2)
    t1 = tri_fusion(T[:m])
    t2 = tri_fusion(T[m:])
    return fusion_2(t1,t2)

def main():
    t1 = [randint(0,10**1) for _ in range(10**1)]
    t2 = [randint(0,10**1) for _ in range(10**1)]
    t1.sort()
    t2.sort()
    print(t1)
    print(t2)
    print(fusion(t1,t2))
    print(fusion_2(t1,t2))
    T = [randint(0,10**1) for _ in range(10**1)]
    print(T)
    print(tri_fusion(T))
    T.sort()
    print(T)
    

if __name__ == '__main__':
    main()