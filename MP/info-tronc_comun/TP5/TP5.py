# 1. (q**2) *r*p
from math import inf


m1 = 200*10*5 + 10*100*5
m2 = 10*100*200 + 200*100*5
print(m1,m2)

def min_mult(d):
    n = len(d)
    m = [[0 if i == j else inf for j in range(n)] for i in range(n)]
    for j in range(1,n):
        for i in range(1,j):
            m[i][j] = 0 if i == j else min(m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j] for k in range(i,j+1))
    return m[0][n-1]

test = min_mult([5,200,10,100])