def reduit(P):
    while P!= [] and P[-1] == 0:
        P.pop()
    
def degre(P):
    reduit(P)
    return len(P) -1

def monome(a, n):
    P = [0]*n + [a]
    reduit(P)
    return P

def mul_Xn(P,n):
    P=[0]*n + P
    reduit(P)
    return P

def evalue(P,x):
    v = 0
    for i in range(len(P)):
        v += P[i]*(x**i)
    return v

def mult_scalaire(P,a):
    for i in range(len(P)):
        P[i] *= a
    reduit(P)
    return P

def additionne(P,Q):
    P += [0]*(max(len(P),len(Q))-len(P))
    Q += [0]*(max(len(P),len(Q))-len(Q)) 
    T = []
    for i in range(len(P)):
        T.append(P[i]+Q[i])
    reduit(T)
    return T

def soustrait(P,Q):
    P += [0]*(max(len(P),len(Q))-len(P))
    Q += [0]*(max(len(P),len(Q))-len(Q)) 
    T = []
    for i in range(len(P)):
        T.append(P[i]- Q[i])
    reduit(T)
    return T

def multiplie(A,B):
    reduit(A)
    reduit(B)
    AB = [0]*(len(A)+len(B))
    A += [0]*(len(AB)-len(A))
    B += [0]*(len(AB)-len(B))
    for k in range(len(AB)):
        for i in range(0,k):
            AB[k] += A[i]*B[k-i]
    reduit(AB)
    return AB

def main():
    P = [1, 2, 3, 0, 0]
    reduit(P)
    print(P)
    P = []
    reduit(P)
    print(P)
    P = []
    print(degre(P))
    print(monome(5,3))
    print(mul_Xn([1,2,3],2))
    print(evalue([1,2,3],5))
    print(evalue([],5))
    print(mult_scalaire([1,2,3],3))
    print(mult_scalaire([1,2,3],0))
    print(additionne([1,2,3],[4,3,2,1]))
    print(soustrait([1,2,3],[4,3,2,1]))
    print(multiplie([1,2,3],[4,3,2,1]))

if __name__ == "__main__":
    main()