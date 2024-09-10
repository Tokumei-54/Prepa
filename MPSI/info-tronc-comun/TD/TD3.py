from math import pi
from random import random
from time import time

def volume(r):
    return 4/3*pi*r**3

def somme1(n): #converge vers 0.25
    u = 0
    for i in range(1,n):
        u += 1/(i*(i+1)*(i+2))
    return u

def indice_p(): #22
    for p in range(10**3,0,-1):
        if abs(somme1(p)-0.25)>=10**(-3):
            return p+1
    return "error"

def somme_div_naive(n):
    t = time()
    s=0
    for i in range(1,n):
        if i%3==0 and i%5==0:
            s+=i
        #print(i)
    print('n',s , time()-t)
    return s, time()-t

def somme_div(n):
    t = time()
    s=0
    for i in range(0, n,15):
        s+=i
        #print(i)
    print(s , time()-t)
    return s , time()-t


def devinette():
    n=int(random()*100)
    l=0
    h=100
    for _ in range(7):
        guess = int(input(f"Devine un nombre entre {l} et {h} : "))
        if guess == n :
            print("GAGNE")
            return 1
        elif l <= guess < n :
            l = guess
            print('+')
        elif n < guess <= h:
            h = guess
            print('-')
        else:
            print("Error : guess out of scope, you lost a guess for nothing")
    print("PERDU")
    return 0


def main():
    #print(volume(1))
    #print(somme1(10**7))
    #print(indice_p())
    #devinette()
    #print(somme_div_naive(10**10))
    #print(somme_div(10**10))
    bl=0
    tl=0
    bg=0
    tg=0
    for _ in range(10):
        bl,tl = somme_div(10**7)
        bg,tg = somme_div_naive(10**7)
    print(tl/10)
    print(tg/10)


if __name__ == '__main__':
    main()