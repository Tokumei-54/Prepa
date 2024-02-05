import random


def second_maxi(T): #EXERCICE 2
    if T[0]>T[1]:
        max1 , max2 = T[0],T[1]
    else:
        max1 , max2 = T[1],T[0]
    for i in range(2,len(T)):
        if max1<= T[i]:
            max1, max2 = T[i], max1
        elif max2 <=T[i]:
            max2 = T[i]
    return max2

def init_maxi(T,max1,max2,f1,f2,i):
    if i >= len(T)-1:
        return "equal"
    elif T[i]>T[i+1]:
        max1 , max2 = T[i],T[i+1]
        f1 , f2 = i+1,1
        return max1,max2,f1,f2,i
    elif T[i]<T[i+1]:
        max1 , max2 = T[i+1],T[i]
        f1 , f2 = 1,i+1
        return max1,max2,f1,f2,i
    else :
        init_maxi(T,max1,max2,f1,f2,i+1)
        

def second_maxi2(T):    
    if T[0]>T[1]:
        max1 , max2 = T[0],T[1]
        f1 , f2 = 1,1
    elif T[0]<T[1]:
        max1 , max2 = T[1],T[0]
        f1 , f2 = 1,1
    else:
        max1 , max2 = T[0],T[1]
        f1 , f2 = 1,1
        try:
            max1 , max2 , f1 , f2 , n = init_maxi(T,max1,max2,f1,f2,1)
        except: 
            return "error: tout les element de la liste sont égaux"

    for i in range(n+1,len(T)):
        if max1< T[i]:
            max1, max2 = T[i], max1
            f1 , f2 = 1,f1
        elif max1 == T[i]:
            f1+=1
        elif max2 <T[i]:
            max2 = T[i]
            f2 = 1
        elif max2 == T[i]:
            f2+=1
    return max1,f1,max2,f2

def tri_insert(L): #EXERCICE 3
    l = L[:] # +1 operation
    for i in range(1,len(L)):
        j = i # +n operation
        while l[j-1]>l[j] and j>0: # + operation
            l[j-1],l[j] = l[j],l[j-1]
            j-=1
    return l


def main():
    print(second_maxi([1,2,3,54,69,69]))
    print(second_maxi2([1,1,2,3,54,69,69]))
    print(second_maxi2([54,54,54]))
    print(tri_insert([54,69,8,0,42,2023,54]))
    print(tri_insert([]))
    print(tri_insert([0, 8, 42, 54, 54, 69, 2023]))
    print(tri_insert([2023, 69, 54, 54, 42, 8, 0]))

    for i in range(100):
        n = random.randint(1,100)
        m = random.randint(1,100)
        L = [random.randint(0,m) for _ in range(n)]
        #print(i,": ",tri_insert(L))
        #print(i,"sorted() :",sorted(L))
        if tri_insert(L) == sorted(L):
            print("True")
        else:
            print("False")

    
if __name__=='__main__':
    main()