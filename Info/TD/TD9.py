#La fonction test si un nombre est pair 
def pair(n): #Exercice 1
    if n == 0:
        return True
    elif n < 0:
        return False
    else :
        return pair(n-2)

def compte_à_rebours(n):
    return range(0,n+1,-1)

def compte_à_rebours_rec(n):
    if n == 0:
        return (0,)
    else :
        return (n,) + compte_à_rebours_rec(n-1)



def puissances(x,n):
    if n == 0:
        return 1
    x_n = x
    for _ in range(n-1):
        x_n *= x
    return x_n

def puissances_rec(x,n):
    puissances_rec.appels += 1
    if n == 0:
        return 1
    else :
        return x*puissances_rec(x,n-1)
puissances_rec.appels = 0

def puissances_def2(x,n):
    if n == 0:
        return 1
    elif pair(n):
        x_k = 1
        for _ in range(n//2):
             x_k *= x
        return x_k*x_k
    else:
        x_k = 1
        for _ in range(n//2):
             x_k *= x
        return x*x_k*x_k

def puissances_rec_def2(x,n):
    puissances_rec_def2.appels += 1
    if n == 0:
        return 1
    elif pair(n):
        return puissances_rec_def2(x,n//2)**2
    else :
        return x*puissances_rec_def2(x,n//2)**2
puissances_rec_def2.appels = 0

def puissances_def3(x,n):
    if n == 0:
        return 1
    elif pair(n):
        x_k = 1
        for _ in range(n//2):
             x_k *= x*x
        return x_k
    else:
        x_k = 1
        for _ in range(n//2):
             x_k *= x*x
        return x*x_k

def puissances_rec_def3(x,n):
    puissances_rec_def3.appels += 1
    if n == 0:
        return 1
    elif pair(n):
        return puissances_rec_def3(x*x,n//2)
    else :
        return x*puissances_rec_def3(x*x,n//2)
puissances_rec_def3.appels = 0


def syracuze(u0,n): #Exercice 3
    if n == 0:
        return u0
    elif pair(u0):
        return syracuze(u0/2,n-1)
    else :
        return syracuze(3*u0+1,n-1)
    
def collatz(u0,n=0):
    if u0 == 1:
        return n
    elif pair(u0):
        return collatz(u0/2,n+1)
    else :
        return collatz(3*u0+1,n+1)
    

def main():
    print(pair(54))
    print(pair(69))
    print(compte_à_rebours(54))
    print(compte_à_rebours_rec(54))

    
    x = 54
    n = 54
    print(x**n)
    
    print(puissances(x,n))
    print(puissances_rec(x,n))
    print(puissances_rec.appels)
    
    print(puissances_def2(x,n))
    print(puissances_rec_def2(x,n))
    print(puissances_rec_def2.appels)
    
    print(puissances_def3(x,n))
    print(puissances_rec_def3(x,n))
    print(puissances_rec_def3.appels)

    print(syracuze(2,2))
    print(collatz(2))

if __name__=='__main__':
    main()
