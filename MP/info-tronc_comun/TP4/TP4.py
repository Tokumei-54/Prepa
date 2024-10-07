def binom1(n:int , p:int)-> int :
    if p > n :
        return 0
    elif p == 0 or p == n :
        return 1
    elif p == 1 or p ==  n - 1:
        return n 
    else :
        return binom1(n -1, p-1) + binom1(n -1, p)


def binom2(n:int , p:int)-> int:
    C = [[0 for _ in range(p+1)] for _ in range(n+1)]
    C[1][0],C[1][1]= 1,1
    for i in range(2,n+1):
        for j in range(i+1):
            C[i][j] = C[i-1][j-1] +C[i-1][j]
            if i == n and j == p :
                return C[n][p]


def binom3(n:int , p:int)-> int:
    C = [0 for _ in range(p+1)]    
    C[0],C[1]= 1,1
    for i in range(2,n+1):
        for j in range(i-1,-1,-1):
            C[j] = C[j-1] +C[j]
            if i == n and j == p :
                return C[p]

print(binom1(3,2))
print(binom2(3,2))
print(binom3(3,2))