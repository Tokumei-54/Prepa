from math import factorial
from random import randint
from time import time

#Exercice 1

def binom(k,n):
    return factorial(n)/(factorial(k)*factorial(n-k)) 

#Il y a (n-1) + (k - 1) + (n - k - 1) + 2  soit  2n-1  multiplications dans la fonction binom()

def binom_rec(k,n):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    return ((n-k+1)/k)*binom_rec(k-1,n)

#Il y a (n-1) + (k - 1) + (n - k - 1) + 2  soit   2n-1  multiplications dans la fonction binom_rec() 


#Exercice 2 (+4)

# def tri_bulle(T) :
#     for i in range(len(T)-1,0,-1) :
#         for j in range(i) :
#             if T[j] > T[j+1] :
#                 T[j], T[j+1] = T[j+1], T[j]

def tri_bulle(T):
    for i in range(len(T)-1,0,-1):
        p=0
        bulle = 0        
        for j in range(i+1):
            if T[j] > T[bulle] :
                bulle = j
                p+=1
        if p == i :
           break
        T[bulle], T[i] = T[i],T[bulle]


 #Exercice 3

def comptage(T,m):
    C = [0 for _ in range(m+1)]
    for i in T:
        C[i]+=1
    return C

def tri_comptage(T):
    max = T[0]
    for i in range(1,len(T)):
        if T[i] > max :
            max = T[i]
    C = comptage(T,max)
    T = []
    for j in C:
        T+= [j]*C[j]


# def time_test(func,input,iterations=1):
#     t = time()
#     for i in range(iterations):
#         func(*input)
#     return time()-t

def main():
    n = 3
    k = 2
    print(binom(k,n))
    print(binom_rec(k,n))

    T = [randint(0,100) for _ in range(randint(2,20))]
    print(T)
    tri_bulle(T)
    print(T)
    
    T = [randint(0,10) for _ in range(randint(2,20))]
    print(T)
    print(comptage(T,10))


if __name__ == '__main__':
    main()