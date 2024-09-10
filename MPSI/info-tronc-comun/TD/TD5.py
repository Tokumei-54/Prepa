def cherche(L,x): #EXERCICE 1
    for i in range(len(L)):
        if x == L[i]:
            return i
    return False

def maxi(L): #EXERCICE 2
    try :
        max = L[0]
    except:
        return "ValueError: maxi() arg is an empty sequence"
    for i in L:
        if i>= max:
            max = i
    return max

def nb_iter(L,k): #EXERCICE 3
    n=0
    for i in L:
        if i == k:
            n+=1
    return n

def tri_compt(L,m):
    if maxi(L)> m:
        return None
    l=[]
    for i in range(m+1):
        for j in L:
            if j == i:
                for _ in range(nb_iter(L,j)):
                    l.append(j)
                break
    return l

def distance_spe(L): #EXERCICE 4
    l=[]
    for i in L:
        l.append(abs(i[0]+i[1]))
    return l

def tri_plan(L):
    l=[]
    for i in range(maxi(distance_spe(L))+1):
        for j in range(len(distance_spe(L))):
            if distance_spe(L)[j] == i:
                l.append(L[j])
                
    return l



def main():
    print(cherche([0,8,54,100],54))
    #print(cherche([i**2 for i in range(1,20)],55))
    L = [1]
    for i in range(2,21):
        L.append(L[-1]+i**2)
    print(L)
    print(cherche(L,55))
    print(maxi([0,8,54,100]))
    print(maxi([]))
    print(nb_iter([54,0,8,54,100,54],54))
    print(tri_compt([54,0,8,54,100,54],100))
    print(tri_compt([54,0,8,54,100,54],54))
    print(distance_spe([[1,3],[3,-1],[1,-3]]))
    print(tri_plan([[1,3],[3,-1],[1,-4],[54,69],[54,-69]]))
if __name__ == '__main__' :
    main()