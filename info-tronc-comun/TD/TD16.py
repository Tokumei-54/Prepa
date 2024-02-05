#Exercice 1
def ecriture_base(n,B):
    Q , R = divmod(n,B)
    n_b = str(R)
    while Q > 0 :
        Q , R = divmod(Q,B)
        n_b = str(R) + n_b 
    return n_b

# 2. Terminaison Q_i+1 = Q_i//B donc la suite des valeurs de Q est strictemment decroisante donc il exite un rang N tel que Q = 0 donc la boucle se termine

# 3. On admet l'invarient de boucle n_B_i est la representation en base B de jusqu'au chifre des B**i Donc au rang N n_b_N est la repredentation de  n jusqu'au chiffre des B**N or Q = 0 donc la descomposition en base B est est correcte

# 4.  il y a 2+ ln(n)/ln(b) * 2 operation soit un O(ln(n))
def ecriture_base_rec(n,B): 
    if n <= 0 :
        return ''
    else :
        Q , R = divmod(n,B)
        return ecriture_base_rec(Q,B) + str(R)
    
def hex2bin(ch16_n):
    h2b = {'0':'0000', '1':'0001', '2':'0010','3':'0011', '4': '0100', '5': '0101', '6':'0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    ch2_n = ''
    for i in ch16_n:
        ch2_n += h2b[i]
    return ch2_n

def int2hex(n):
    i2h = {0 : '0', 1: '1', 2 : '2', 3 : '3', 4 : '4 ', 5 : '5', 6 : '6', 7 : '7', 8 : '8' , 9 : '9', 10 : 'A', 11: 'B', 12 :'C', 13 : 'D', 14 : 'E',15:'F'}
    ch16_n = ''
    k = 0
    while n - 16**(k+1) > 0:
        k += 1

    while k >= 0 :
        l = 0 
        while n - (l+1)*(16**k) >= 0:
            l += 1
        ch16_n += i2h[l]
        n -= l*(16**k)
        k -= 1
    return ch16_n

def change_base(ch_n,B1,B2):
    n = 0
    for i in range(len(ch_n)):
        n += int(ch_n[i])*(B1**(len(ch_n)-1-i))
    Q , R = divmod(n,B2)
    n_B2 = str(R)
    while Q > 0 :
        Q , R = divmod(Q,B2)
        n_B2 = str(R) + n_B2 
    return n_B2

def somme(n,m,):
    if len(n) > len(m) :
        m = '0'*(len(n)-len(m)) + m
    elif len(m) > len(n) :
        n = '0'*(len(m)-len(n)) + n
    nm = ''
    c='0'
    for i in range(len(n)-1,-1,-1):
        if c ==  '0':
            if n[i] == m[i] == '0':
                nm = '0' + nm
            elif n[i] == m[i] == '1':
                nm = '0' + nm
                c = '1'
            else :
                nm = '1' + nm
        else :
            if n[i] == m[i] == '0':
                nm = '1' + nm
                c = '0'
            elif n[i] == m[i] == '1':
                nm = '1' + nm
                c = '1'
            else :
                nm = '0' + nm
                c = '1'
    if c == '1':
        nm = '1' + nm
    return nm
            

def multiplie(n,m) :
    nm=''
    snm = []
    for i in range(len(m)):
        if m[i] == '1':
            snm.append(n + '0'* i)
    for j in snm:
        nm = somme(nm,j)
    return nm



        
    

def main():
    print(ecriture_base(4,2))
    print(ecriture_base_rec(4,2))
    print(hex2bin('36'))
    print(int2hex(54))
    print(change_base('54',10,2))
    print(somme('1101','101001'))
    print(multiplie('110','1001'))




if __name__ == '__main__':
    main()