import copy


def selection_optimale(E):
    def debut(x):
        return x[0]
    def fin(x):
        return x[1]
    L = copy.deepcopy(E)
    L.sort(key=fin)
    Act = [L[0]]
    for act in L[1:] :
        if debut(act) >= fin(Act[-1]) :
            Act.append(act)
    return len(Act)


#O(sort(key=fin) + O(n)
#

def est_libre(L,h):
    indice= 0
    for i in range(len(L)):
        if h - L[i][-1][1] > h - L[indice][-1][1] :
            indice = i
    return indice if h - L[indice][-1][1] >= 0 else -1

def allocation(C):
    def fin(x):
        return x[1]
    K = copy.deepcopy(C)
    K.sort(key=fin)
    L = [[K[0]]]
    for k in K :
        i = est_libre(L,k[0])
        if i >= 0 :
            L[i].append(k)
        else :
            L.append([k])
    return L





def main():
    print(selection_optimale([(1,7),(3,4),(1,2),(6,8),(2,5),(2,3),(4,7)]))
    print(allocation([(1,7),(3,4),(1,2),(6,8),(2,5),(2,3),(4,7)]))

if __name__ == "__main__" :
    main()