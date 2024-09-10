import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from cmath import rect, pi

#Exercice 1
#1. soit I le milieu de A B , I = (A + B) / 2 
#2. \vec(AB)= B-A
#3. z' = |z|exp(arg(z)+\alpha) 
#4. B = |A|exp(arg(A)+\pi/3) = 1 exp(\pi / 2 + 2\pi / 3) = exp(7\pi/6)
#   C = |B|exp(arg(B)+\pi/3) = 1 exp(5\pi / 6 + 2\pi / 3) = exp(11\pi/6)

#Exercice 2

def courbe(x,y):
    plt.plot(x, y, 'b', linewidth = 0.2)
    plt.axis('equal')
    plt.show()

#1. zc = (2za + zb) / 3    ze = (2zb + za)/ 3       zd =  (|(2za - zb)/ 3 - za|exp(arg((2za - zb)/ 3 - za)+\pi/3)) + (2za + zb) / 3 
#2.
def flocon_de_Koch(n=8,A=1j,B=rect(1, -pi/6),C=rect(1, -5*pi/6), r=rect(1, pi/3)):
    P = [B, C, A]
    if n:
        a = A
        for _ in range(n):
            Q = []
            for b in P:
                c, e = (2*a + b) / 3, (2*b + a) / 3
                d = r*(c-a)+c
                a = b
                Q += [c,d,e,b]
            P = Q
    x = [z.real for z in P]
    y = [z.imag for z in P]
    courbe(x,y)

#Exercice 3

def flocon_de_Koch_rec(n=8,A=1j,B=rect(1, -pi/6),C=rect(1, -5*pi/6), r=rect(1, pi/3)):
    x, y = [0], [1]
    def branche(a, b, n):
        if n:
            c, e = (2*a + b) / 3, (2*b + a) / 3
            d = r*(c-a)+c
            branche(a, c, n - 1)
            branche(c, d, n - 1)
            branche(d, e, n - 1)
            branche(e, b, n - 1)
        else:
            x.append(b.real)
            y.append(b.imag)
    branche(A, B, n)
    branche(B, C, n)
    branche(C, A, n)
    courbe(x,y)

#Exercice 4
def xy(A): return A.real, A.imag
def triangle(A, B, C, c,ax):
    ax.add_patch(Polygon([xy(A), xy(B), xy(C)],color = c, fill = True, linewidth = 0.2))

#1. i = (a+c)/2   j = (a+b)/2    k = (c+b)/2

#2. 
def Triangle_de_serpinsky(n=8,A=1j,B=rect(1, -pi/6),C=rect(1, -5*pi/6)):
    ax = plt.figure().add_subplot()
    triangle(A, B, C, 'black',ax)
    if n :
        T = [((A + C) / 2, (A + B)/2, (C + B)/2)]
        for m in range(n - 1):
            for a, b, c in T[-3**m:]:
                d, e, f = (a + c) / 2, (a + b)/2, (c + b)/2
                T.append((d-(b-a)/2,d,d+(c-b)/2))
                T.append((e,e+(b-a)/2,e+(c-a)/2))
                T.append((f-(c-a)/2,f-(c-b)/2,f))
        for t in T:
            triangle(*t, 'white',ax)
    plt.axis('equal')
    plt.show()

def Triangle_de_serpinsky_rec(n=8,A=1j,B=rect(1, -pi/6),C=rect(1, -5*pi/6)):
    ax = plt.figure().add_subplot()
    def sierpe(A, B, C, n):
        if n:
            I, J, K = (A + C) / 2, (A + B)/2, (C + B)/2
            triangle(I, J, K, 'white',ax)
            sierpe(I + J - K, J ,I , n - 1)
            sierpe(J,J + K - I ,K , n - 1)
            sierpe(I,K ,K + I - J , n - 1)
    triangle(A, B, C,'black',ax)
    sierpe(A, B, C, n)
    plt.axis('equal')
    plt.show()


def main():
    #flocon_de_Koch()
    #flocon_de_Koch_rec()
    Triangle_de_serpinsky_rec()

if __name__ == "__main__":
    main()