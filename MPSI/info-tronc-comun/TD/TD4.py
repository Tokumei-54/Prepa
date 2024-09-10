from math import exp , cos, ceil

#EXERCICE 1
def derive(f,a,h=1e-5):
    return (f(a+h)-f(a-h))/(2*h)

def tangeante(f,a,h=1e-5):
    return (derive(f,a,h),-derive(f,a,h)*a+f(a))

def derive_compose(f,g,a,h=1e-5):
    return derive(g(f()),a,h)

#EXERCICE 2
def question1():
    print(range(1,11))
    print(range(1,1001))

def liste1(n):
    return range (2,n,2)

def liste2(liste):
    for element in liste:
        print(element)

def liste3(liste,i):
    try:
        liste[i-1]*=2
    except:
        print("IndexError: list index out of range")
    return liste

#EXERCICE 3
def retourne(list):
    for i in (range(ceil(len(list)/2))):
        list[i],list[-(i+1)]=list[-(i+1)],list[i]
    return list

def is_palindrome(objet):
    return list(objet) == retourne(list(objet))

def main():
    print(derive(lambda x : x**2, 0))
    print(derive(lambda x : exp(x), 0))
    print(tangeante(lambda x : x**2, 0))
    print(tangeante(lambda x : cos(x), 0))
    print(liste3([1,2,3],4))
    print(list(12321))
    print(retourne(list(12321)))
    print(is_palindrome(12321))
if __name__=='__main__':
    main()