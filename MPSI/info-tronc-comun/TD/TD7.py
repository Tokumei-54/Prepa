from copy import deepcopy

LomremIpsum = " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit. Ut velit mauris, egestas sed, gravida nec, ornare ut, mi. Aenean ut orci vel massa suscipit pulvinar. Nulla sollicitudin. Fusce varius, ligula non tempus aliquam, nunc turpis ullamcorper nibh, in tempus sapien eros vitae ligula. Pellentesque rhoncus nunc et augue. Integer id felis. Curabitur aliquet pellentesque diam. Integer quis metus vitae elit lobortis egestas. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi vel erat non mauris convallis vehicula. Nulla et sapien. Integer tortor tellus, aliquam faucibus, convallis id, congue eu, quam. Mauris ullamcorper felis vitae erat. Proin feugiat, augue non elementum posuere, metus purus iaculis lectus, et tristique ligula justo vitae magna. Aliquam convallis sollicitudin purus. Praesent aliquam, enim at fermentum mollis, ligula massa adipiscing nisl, ac euismod nibh nisl eu lectus. Fusce vulputate sem at sapien. Vivamus leo. Aliquam euismod libero eu enim. Nulla nec felis sed leo placerat imperdiet. Aenean suscipit nulla in justo. Suspendisse cursus rutrum augue. Nulla tincidunt tincidunt mi. Curabitur iaculis, lorem vel rhoncus faucibus, felis magna fermentum augue, et ultricies lacus lorem varius purus. Curabitur eu amet."

def recherche_naive(motif,texte): #EXERCICE 1
    def occurence(i):
        return motif == texte[i:i+len(motif)]
    for j in range(len(texte)-len(motif)):
        if occurence(j):
            return True
    return False

def Min_et_max(L): #EXERCICE 2
    min , max = L[0], L[0]
    for i in L:
        if i < min:
            min = i
        if i> max:
            max = i
    return min , max

def cherche_proche(T):
    assert len(T)>= 2 , "la liste ne contient pas aller d'éléments" 
    dist = abs(Min_et_max(T)[0] - Min_et_max(T)[1])
    proche = Min_et_max(T)
    for i in range(len(T)):
        for j in range (len(T)):
            if abs(T[i]-T[j])< dist and i!=j:
                dist = abs(T[i]-T[j])
                proche = (T[i],T[j])
    return proche

#EXERCICE 3
#empty field : ' '  illigal field : '·'   Queen : '●'  

def display(board):
    for rows in board:
        row = ""
        for field in rows:
            row+='['+field+']'
        print(row)
    print('')

def is_legal(board):
    #display(board)
    Q = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == '●':
                Q.append((row,col))
    board = [[' ' for _ in range(len(board[n]))] for n in range(len(board))]
    #display(board)
    for q in Q:
        i,j = q
        if board[i][j] == ' ':
            board[i][j] = '●'
        else:
            return False , board
        #display(board)

        for a in range(len(board[i])):
            if a != j :
                if board[i][a] == '●':
                    return False , board
                else:
                    board[i][a] = '·'
        #display(board)

        for b in range(len(board)):
            if b != i :
                if board[b][j] == '●':
                    return False , board
                else:
                    board[b][j] = '·'
        #display(board)

        for c in range(len(board)):
            for d in range(len(board[c])):
                if (c != i and d != j) and (c + d == i + j or  c + len(board)-1-d == i + len(board)-1-j):
                    if board[c][d] == '●':
                        return False , board
                    else:
                        board[c][d] = '·'
        #display(board)

    return True , board


def queen_configuration(board = [[' ' for _ in range(8)] for __ in range(8)],n = 8):
    #display(board)
    if n == 0:
        return board, True
    for i in range(1,len(board)):
        for j in range(len(board[i])):
            board = is_legal(board)[1]
            if board[i][j] == ' ' and is_legal(board)[0]:
                board[i][j] = '●'
                board, test = queen_configuration(board,n-1)
                if test:
                    return board ,True
                else:
                    board[i][j] = '·'
    return board, False
    


def main():
    print(LomremIpsum[1:1+len("Lorem")])
    print(recherche_naive("Lorem",LomremIpsum))
    print(recherche_naive("Maecenas",LomremIpsum))
    print(recherche_naive("Informatique",LomremIpsum))
    print(Min_et_max([0,1.54,54,-69,2048]))
    print(cherche_proche([0,1.54,54,-69,2048]))
    #print(cherche_proche([0]))

    échéquier = [[' ' for _ in range(8)] for __ in range(8)]

    échéquier[5][4] = '●'
    échéquier[0][0] = '●'
    print(échéquier)
    display(échéquier)
    print(is_legal(échéquier)[0])
    display(is_legal(échéquier)[1])

    échéquier = [[' ' for _ in range(8)] for __ in range(8)]
    display(queen_configuration(échéquier)[0])
if __name__=='__main__':
    main()