from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def composante_rouge(im):
    tab = np.array(im)
    a, b, c = tab. shape
    for i in range(a):
        for j in range(b):
            tab[i][j][1], tab[i][j][2] = 0 , 0
    return Image.fromarray(tab)

def composante_vert(im):
    tab = np.array(im)
    a, b, c = tab. shape
    for i in range(a):
        for j in range(b):
            tab[i][j][0], tab[i][j][2] = 0 , 0
    return Image.fromarray(tab)

def composante_bleu(im):
    tab = np.array(im)
    a, b, c = tab. shape
    for i in range(a):
        for j in range(b):
            tab[i][j][0], tab[i][j][1] = 0 , 0
    return Image.fromarray(tab)

def negatif(im):
    tab = np.array(im)
    a, b, c = tab. shape
    for i in range(a):
        for j in range(b):
            tab[i][j]= 255 - tab[i][j][0] , 255 - tab[i][j][1] , 255 - tab[i][j][2] 
    return Image.fromarray(tab)

def cadre_noir_int(im,ep):
    tab = np.array(im)
    a, b, c = tab. shape
    for i in range(ep):
        for j in range(a):
            tab[i][j]= [0,0,0]
            tab[-i-1][j]= [0,0,0]
        for k in range(b):
            tab[k][i]= [0,0,0]
            tab[k][-i-1]= [0,0,0]
    return Image.fromarray(tab)

def cadre_noir_ext(im,ep):
    tab = np.array(im)
    a, b, c = tab. shape
    cadre =  np.zeros((a+2*ep,b+2*ep,c), dtype='uint8')
    for i in range(a):
        for j in range(b):
            cadre[i+ep][j+ep] = tab[i][j]
    return Image.fromarray(cadre)





im = Image.open("/home/eleve/Dokuments/Prepa/info-tronc-comun/TD/lena.png")
print("Mode des couleurs de l'image : ", im.mode)
print("Format de l'image : ", im.format)
print("Taille de l'image : ", im.size)
print("Infos de l'image : ", im.info)

im.show()

tab = np.array(im)
print("Taille du tableau : ", tab.shape)
print("Type des valeurs : ", tab.dtype)


nouv_im = Image.fromarray(tab)
nouv_im.show()
nouv_im.save("nouvelle_image.png")

composante_rouge(im).save("rouge.png")
composante_vert(im).save("vert.png")
composante_bleu(im).save("bleu.png")
negatif(im).save("negatif.png")
cadre_noir_int(im,5).save("cadre_noir_int.png")
cadre_noir_ext(im,5).save("cadre_noir_ext.png")

im.close()

h, l = 512, 512
nouv_tab = np.zeros((h,l,3), dtype='uint8')
Image.fromarray(nouv_tab).show()


