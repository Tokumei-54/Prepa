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

def niveau_gris(im):
    tab = np.array(im)
    a, b, c = tab. shape
    cadre =  np.zeros((a,b), dtype='uint8')
    for i in range(a):
        for j in range(b):
            cadre[i][j] = 0.299 * tab[i][j][0] + 0.587 * tab[i][j][1] + 0.114 * tab[i][j][2]
    return Image.fromarray(cadre)

def pixelisation(im,n):
    tab = np.array(im)
    x, y, c = tab.shape
    for i in range(x//n):
        for j in range(y//n):
            r, g, b = 0 ,0 ,0
            for k in range(n):
                for l in range(n):
                    r += tab[i * n + k][j * n + l][0]
                    g += tab[i * n + k][j * n + l][1]
                    b += tab[i * n + k][j * n + l][2]
            r, g, b = r/n**2, g/n**2, b/n**2
            for p in range(n):
                for q in range(n):
                    tab[i * n + p][j * n + q] = [r,g,b]
    return Image.fromarray(tab)

def histo(im):
    tab = np.array(im)
    h = [0]*256
    for ligne in tab:
        for i in ligne:
            h[i] += 1
    return h

def extrait(im, xhg, yhg, xbd, ybd):
    tab = np.array(im)
    a, b, c = tab. shape
    x , y = xbd - xhg, ybd - yhg
    cadre =  np.zeros((x, y, c), dtype='uint8')
    for i in range(x):
        for j in range(y):
            cadre[i][j]= tab[xhg+i][yhg+j]
    return Image.fromarray(cadre)

def luminosite(im, a):
    def f(x):
        return 255 * (x/255)**(1-a)
    tab = np.array(im)
    x, y, c = tab. shape
    for i in range(x):
        for j in range(y):
            tab[i][j]= f(tab[i][j][0]) ,f(tab[i][j][1]) , f(tab[i][j][2])
    return Image.fromarray(tab)

def contraste_plus(im):
    def f(x):
        return 255 /2  * (1 + np.sin((x/255- 1/2)* np.pi))
    tab = np.array(im)
    x, y, c = tab. shape
    for i in range(x):
        for j in range(y):
            tab[i][j]= f(tab[i][j][0]) ,f(tab[i][j][1]) , f(tab[i][j][2])
    return Image.fromarray(tab)

def contraste_moins(im):
    def f(x):
        return (255 / np.pi) * np.arcsin((2/255)*x-1)+255/2
    tab = np.array(im)
    x, y, c = tab. shape
    for i in range(x):
        for j in range(y):
            tab[i][j]= f(tab[i][j][0]) ,f(tab[i][j][1]) , f(tab[i][j][2])
    return Image.fromarray(tab)

def popart(im):
    def filtre(im,f)
        tab = np.array(im)
        x, y, c = tab. shape
        for i in range(x):
            for j in range(y):
                if 
        
    
    return 

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

# composante_rouge(im).save("rouge.png")
# composante_vert(im).save("vert.png")
# composante_bleu(im).save("bleu.png")
# negatif(im).save("negatif.png")
# cadre_noir_int(im,5).save("cadre_noir_int.png")
# cadre_noir_ext(im,5).save("cadre_noir_ext.png")
# niveau_gris(im).save("niveau_gris.png")
# pixelisation(im,8).save("pixelisation.png")
# import matplotlib.pyplot as plt
# plt.plot(histo(niveau_gris(im)))
# plt.show()

# im.close()

# h, l = 512, 512
# nouv_tab = np.zeros((h,l,3), dtype='uint8')
# Image.fromarray(nouv_tab).show()
# extrait(im, 180, 190, 419, 379).save("extrait.png")
# luminosite(im, 0.5).save("luminosité.png")
# luminosite(im, -1).save("luminosité2.png")
contraste_plus(im).save("contraste_plus.png")
contraste_moins(im).save("contraste_moins.png")