

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
    c = np.zeros((x,y), dtype='uint8')
    n , _   = b.shape
    k = n//2
    for i in range(1,x-1):
        for j in range(1,y-1):
            for i_1 in range(n):
              for j_1 in range(n):
                  c[i][j]+= a[i-k+i_1][j-k+j_1] * b[i_1][j_1]
    return Image.fromarray(c)
                  


def main():
    contours(im,20).save("contours.png")
    convolution(im,np.array([[1,1,1],[1,1,1],[1,1,1]])/9).save("convolution.png")
    
if __name__ == '__main__':
    main()


