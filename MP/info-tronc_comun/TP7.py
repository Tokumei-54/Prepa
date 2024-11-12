# 1 0
# 2 tij = min (ti-1j,tij-1,ti-1j-1) +1
# on initialise à mij

import numpy as np
from random import random

def pgc1_1(M):
    n ,p = np.shape(M)
    T = M[:]
    im,jm,m = 0,0,M[0][0]

    for i in range(1,n):
        for j in range(1,p):
            T[i][j] = min(T[i-1][j],T[i][j-1],T[i-1][j-1]) + 1
            if T[i][j] > m :
                im,jm,m = i,j,T[i][j]
    
    return T,im,jm,m

    
    return T

def pgc1_2(M):
    n ,p = np.shape(M)
    im,jm,m = 0,0,M[0][0]
    T = [[M[i][j] if i ==1 or j ==1 else -1 for j in range(p)]for i in range(n)]

    def t(i,j):
        if T[i][j] == -1:
            T[i][j] = min(t(i-1,j),t(i,j-1),t(i-1,j-1)) + 1
            if T[i][j] > m :
                im,jm,m = i,j,T[i][j]
        return T[i][j]
    
    t(n-1,p-1)
    return T,im,jm,m

def rnd_mat (n,p) :
    M = np.ndarray((n,p), dtype=np.uint8)
    for i in range(n):
        for j in range(p):
            M[i][j] = np.uint8(random()<0.85)
    return M

n,p = 10,20
M = rnd_mat(n,p)
T,im,jm,m = pgc1_1(M)
T2,im2,jm2,m2 = pgc1_2(M)
print(M,"\n\n",T,"\n",(im,jm),m,M[im-m:im,jm-m:jm])
print("\n\n",T2,"\n",(im2,jm2),m2,M[im2-m2:im2,jm2-m2:jm2])
T2,im2,jm2,m2 = pgc1_2(M)
print(M,"\n\n",T,"\n",(im,jm),m,M[im-m:im,jm-m:jm])
print("\n\n",T2,"\n",(im2,jm2),m2,M[im2-m2:im2,jm2-m2:jm2])