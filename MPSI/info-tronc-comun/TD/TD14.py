H = open("Info\TD\Hamlet_fr.txt", mode='r', encoding="utf8")
# n=0
# while n<=20 :
#     l =H.readline()
#     if l!='\n':
#         print(l)
#         n+=1

caractères = ['FRANCISCO.', 'BERNARDO.', 'HORATIO.', 'HAMLET.', 'MARCELLUS.',
'LE ROI.', 'LA REINE.', 'OPHÉLIA.', 'LAERTES.', 'POLONIUS.',
'REYNALDO.', 'ROSENCRANTZ.', 'GUILDENSTERN.', 'VOLTIMAND.',
'OSRICK.', 'FORTINBRAS.']

interventions = {K:0 for K in caractères}

def CC(T,D):
    for l in T.readlines():
        for K in D:
            if K == l[:len(K)]:
                D[K]+=1
    return D


def mise_en_forme(mot) :
    mot = mot.strip(';:,?!()0123456789.«»')
    mot = mot.split("'")[-1]
    mot = mot.replace('-',' ')
    mot = mot.replace('—',' ')
    mot = mot.replace('_',' ')
    mot = mot.replace("'",' ')
    mot = mot.lower()
    return mot



mots = []
for l in H.readlines():
    for mot in l.split():
        mots.append(mise_en_forme(mot))

occurence_mots = {}

for mot in mots:
    if mot in occurence_mots:
        occurence_mots[mot]+=1
    else :
        occurence_mots[mot] =1
    
def occurence_max(d):
    max = 0
    mot = ''
    for c,v in d.items() :
        if v > max :
            mot, max = c,v
    return mot, max

mots_200 = [(c,v) for c,v in occurence_mots.items() if v >= 200]

def main():
    print(CC(H,interventions))
    print(mise_en_forme("d'artillerie.)"))
    print(len(occurence_mots))
    print(occurence_max(occurence_mots))
    print(mots_200)

if __name__ == '__main__':
    main()

