import math
import numpy as np
import matplotlib.pyplot as plt

def Exercice_1():
    help(math)
    help(math.floor)
    help(math.ceil)
    #degrees() / radians()
    #e et pi 

def degrees(x):
    return x*180/math.pi

def radians(x):
    return x*math.pi/180

def trace_de_coubes():
    #plt.xlim(xmin, xmax)
    #plt.ylim(ymin, ymax)
    pi = np.pi
    X = np.linspace(-pi/2, pi/2, 100)
    Y_sin = np.sin(X)

    Y_tan = np.tan(X)
    plt.plot(X, Y_sin, 'bo', label='sin(x)')
    plt.plot(X, np.cos(X), 'g-', label='cos(x)')
    plt.plot(X, Y_tan, 'ro', label='tan(x)')
    plt.plot(X, X, '-.', label='cos(x)')

    plt.title('Tracé de la fonction')
    plt.ylim(-pi, pi)
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.grid(linestyle='-.')
    plt.legend() 
    plt.show()

def Exercice_3():
    pi = np.pi
    x = np.linspace(-pi/2, pi/2, 30) #np.linspace(-pi/2, pi/2, 30) renvoie un tableau de n valeurs régulièrement réparties sur l’intervalle [-pi/2, pi/2]
    y = np.sin(x) #prend en entré plusieur ellement comme un tableau. ufunc : une fonction qui opere sur un ndarray element-wise : qui opere element par element standard broadcasting : adapte les element de nparray
    plt.title('Tracé de la fonction sinus avec Numpy')
    plt.plot(x,y,'bo',label='np.sin(x)')
    plt.legend()
    plt.show()

def Exrecice_4_1():
    x = np.linspace(-1,1,100)
    for n in [2,3,4,5,10]:
        plt.plot(x,x**n,label=f"x^{n}")
    plt.legend()
    plt.grid(linestyle='-.')
    plt.show()

def Exrecice_4_2():
    x = np.linspace(-1,3,100)
    plt.plot(x,1+2*x)

    for n in [2,3,4,5]:
        plt.plot(x,1+2*x+(x-1)**n)
        #print(n,1+2*0+(0-1)**n) #les valeurs sont respectivement {1,2,0,2,0} 
    plt.grid(linestyle='-.')
    plt.show()


def main():
    #Exercice_1()
    print(degrees(math.pi))
    print(radians(180))
    print(degrees(radians(180)))
    
    #trace_de_coubes()

    #Exercice_3()
    x = np.linspace(-np.pi/2, np.pi/2, 30)
    print(type(x))
    print(type(list(x)))
    #help(np.sin)

    #Exrecice_4_1() #Vvariation des fontion x^n
    Exrecice_4_2()



    
    

if __name__ == '__main__' :
    main()