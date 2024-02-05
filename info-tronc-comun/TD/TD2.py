from math import cos

def Exercice_1() : #EXERCICE 1
    print("Question 1: ")
    for i in range(1,11):
        if i%2!=0:
            print(i)
    
    print("Question 2: ")
    for j in range(100):
        if j%7==0:
            print(j)

    print("Question 3: ")
    n = int(input("Insérer un entier : "))
    for k in range(2,7):
        print(abs(n)*k)

def Exercice_2() : #EXERCICE 2
    print("Question 1: ")
    u=1
    for l in range(100):
        u=cos(u)
    print(u)
    v=1
    s=0
    print("Question 2: ")
    for m in range(1001):
        v=cos(v)
        s+=v
    print(s)

     
def syracuse(n): #Question 1
    while n != 1:
        if n%2 == 0:
            n/=2
        else:
            n=3*n+1
        print(n)

def indice1(n): #Question 2
    indice=0
    while n != 1:
        if n%2 == 0:
            n/=2
        else:
            n=3*n +1
        indice+=1
    return indice

def Exercice_3() : #EXERCICE 3
    print("Question 3: ")
    for n in range(1,1001):
        if indice1(n)> 170:
            print(n)
    print("Question 4: ")
    e=0
    for o in range(1,10001):
        if indice1(o)> 250:
            e+=1
    print(e)
    print("Question 5: ")
    mk=[1]
    p = 1
    while len(mk)<20:
        if indice1(p) > indice1(mk[-1]):
            mk.append(p)
            print(p)
        p+=1
    print(mk)


        


def main():
    print("Exercice 1: ")
    Exercice_1()
    print("Exercice 2: ")
    Exercice_2()
    print("Exercice 3: ")
    Exercice_3()

if __name__ == '__main__':
    main()
