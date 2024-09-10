# 538 : 0000001000011010
#-538 : 1111110111100110

def complement_a_deux(n,N):
    def ecriture_base(n,B,N):
        Q , R = divmod(n,B)
        n_b = str(R)
        while Q > 0 :
            Q , R = divmod(Q,B)
            n_b = str(R) + n_b 
        return '0'*(N-len(n_b))+n_b
    if n >= 0:
        return ecriture_base(n,2,N)
    else:
        return ecriture_base(2**N + n,2,N)
    
def c2N_to_decimal(ch,N):
    n = int(ch,2)
    if n < 2**(N-1):
        return n
    else :
        return n - 2**N
    
def triangle1(n) :
    print('* '*n)
    if n > 0 :
        triangle1(n-1)

def triangle2(n) :
    if n>0 :
        triangle2(n-1)
    print('* '*n)

def figure1(n=3):
    print('* '*n)
    if n>1 :
        figure1(n-1)
    else:
        print('')
    print('* '*n)

def figure2(n=3,m=2):
    print('* ')
    print('* '*(m))
    if m +1 < n:
        figure2(n,m+1)
    else: 
        print('* ')
        print('* '*n)
        print('* ')
    print('* '*(m))
    print('* ')
    

def figure3(n=4,N=30,e=4):
    print('='*n + ' '*e + '='*(N-e-n))
    if n>1 :
        figure3(n-1)
    else:
        print('')
    print('='*n + ' '*e + '='*(N-e-n))

def figure4(c1='m',c2='-',l=11,L=20):
    print(c1*L)
    for i in range(l-2):
        print(c1+c2*(L-2)+c1)
    print(c1*L)




def main():
    print(complement_a_deux(538,16))
    print(complement_a_deux(-538,16))
    print(c2N_to_decimal('0000001000011010',16))
    print(c2N_to_decimal('1111110111100110',16))
    figure1(3)
    print('')
    figure2(25)
    print('')
    figure3(4)
    print('')
    figure4('m','-',11,20)
    

if __name__ == '__main__':
    main()
