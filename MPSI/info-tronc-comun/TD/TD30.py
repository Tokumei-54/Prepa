from random import randint


def partition(t, g, d):
    p = g
    for i in range(g+1,d+1):
        if t[i] <= t[g] :
            p += 1
            t[i] , t[p] = t[p], t[i]
    t[g], t[p] = t[p], t[g]
    return p

def tri_rapide(T):
    def tri(g,d):
        if g < d:
            m = partition(T,g,d)
            tri(g,m-1)
            tri(m+1,d)
    tri(0,len(T) - 1)

def tri_rapi2(T):

    def part(g,d):
        p = randint(g,d)
        T[g], T[p] = T[p], T[g]
        p = g
        for i in range(g+1,d+1):
            if T[i] <= T[g] :
                p += 1
                T[i] , T[p] = T[p], T[i]
        T[g], T[p] = T[p], T[g]
        return p
    
    def tri(g,d):
        if g < d:
            m = partition(T,g,d)
            tri(g,m-1)
            tri(m+1,d)

    tri(0,len(T) - 1)

def partition2 (T,g,d):
        p = randint(g,d)
        T[g], T[p] = T[p], T[g]
        p = g
        g+=1
        while g < d:
            while T[g] <= T[p]:
                g+=1
            while T[d] > T[p]:
                d-=1
            T[g], T[d] = T[d], T[g]
            g += 1
            d -= 1
        T[d], T[p] = T[p], T[d]
        return d
             
        return p

def main():
    T = [0,5,4,8,7,9,2,1,6,3]
    print(partition2(T,0,9))
    # tri_rapi2(T)
    print(T)z

if __name__ == '__main__':
    main()