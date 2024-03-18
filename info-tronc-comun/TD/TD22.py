

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("/home/eleve/Dokuments/Prepa/info-tronc-comun/TD/lena.png")

def contours(im,s=20):
    def e(t,i,j,c):
        return np.sqrt((float(t[i][j-1][c])-float(t[i][j+1][c]))**2 + (float(t[i-1][j][c])-float(t[i+1][j][c]))**2)
    
    tab = np.array(im)
    x, y, _ = tab. shape
    con = np.full((x,y),255, dtype='uint8')
    
    for i in range(1,x-1):
        for j in range(1,y-1):
            e_p = (e(tab,i,j,0)+e(tab,i,j,1)+e(tab,i,j,2))/3 
            if e_p >= s :
                con[i][j]= 0
    return Image.fromarray(con)

def convolution(im,b):
    a = np.array(im)
    x , y , _ = a.shape
    c = np.zeros((x,y,3), dtype='uint8')
    n , _   = b.shape
    k = n//2
    for i in range(k,x-k):
        for j in range(k,y-k):
            for rgb in range(3):
                pixel_sum = 0
                for i_1 in range(n):
                    for j_1 in range(n):
                        pixel_sum += a[i - k + i_1][j - k + j_1][rgb] * b[i_1][j_1]
                c[i][j][rgb] = max(0, min(pixel_sum, 255))
    return Image.fromarray(c)

def netteté(im):
    return convolution(im,np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]))

def niveau_gris(im):
    tab = np.array(im)
    a, b, c = tab. shape
    cadre =  np.zeros((a,b), dtype='uint8')
    for i in range(a):
        for j in range(b):
            cadre[i][j] = 0.299 * tab[i][j][0] + 0.587 * tab[i][j][1] + 0.114 * tab[i][j][2]
    return Image.fromarray(cadre)

def convolution2(im, b):
    tab = np.array(niveau_gris(convolution(im,b)))
    a, b = tab.shape
    cadre =  np.zeros((a,b), dtype='uint8')
    for i in range(a):
        for j in range(b):
            cadre[i][j] = 255 - tab[i][j]
    return Image.fromarray(cadre)

def contours2(im):
    # b=np.array([[1,1,1],[1,-8,1],[1,1,1]])
    b=np.array([[1,1,1,1,1],[1,1,1,1,1],[1,1,-24,1,1],[1,1,1,1,1],[1,1,1,1,1]])
    return convolution2(im, b)

def rotation(im):
    def rota(tab):
        n,_,_ = tab.shape
        if n <= 2 :
            return tab
        m = n//2
        return np.concatenate(np.concatenate((rota(tab[m:][:m]),rota(tab[m:][m:])), axis=1),np.concatenate((rota(tab[:m][:m]),rota(tab[m:][:m])), axis=1))
    tab = np.array(im)
    return Image.fromarray(rota(tab))
    



def main():
    # contours(im,20).save("contours.png")
    # b_3_9 = np.array([[1,1,1],[1,1,1],[1,1,1]])/9
    # b_5_25 = np.array([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])/25
    # convolution(im,b_5_25).save("convolution.png")
    # netteté(im).save("netteté.png")
    # contours2(im).save("contour2.png")
    rotation(im).save("rotation.png")
    
if __name__ == '__main__':
    main()


