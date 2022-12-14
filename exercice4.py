import random
tab=[["-","-","-"],["-","-","-"],["-","-","-"]]
n=random.randint(0,1) 
def virefier(list):
    for i in list:
        for item in i :
            if item=="-":
                return False
    return True
def gagné(list,player):
    n=len(list)
    gagné=None
    #pour tcheck les lignes: 
    for i in range(n):
        gagné=True
        for j in range(n):
            if list[i][j]!=player:
                gagné=False
                break
        if gagné:
            return gagné
    #pour tcheck les colones: 
    for i in range(n):
        gagné=True
        for j in range(n):
            if list[j][i]!=player:
                gagné=False
                break
        if gagné:
            return gagné
    #pour tcheck les diagonals:
    gagné=True
    for i in range(n):
        if list[i][i]!=player:
            gagné=False
            break
    if gagné:
        return gagné
    ##########
    gagné=True
    for i in range(n):
        if list[i][n-1-i]!=player:
            gagné=False
            break
    if gagné:
        return gagné
        
def Afficher():
    for i in range (len(tab)):
        for j in range(len(tab[0])):
            print(tab[i][j],end=" ")
        print()
def joueur(player):
    if player=="O":
        return "X"
    else:
        return "O"
def ligne_colone_fix(ligne,colone,player):
    tab[ligne-1][colone-1] = player
def demarrer():
    player="X" if n==1 else "O"
    print("-----------welcome to tic tac toe--------------")
    while True:
        
        print(f"tour de joueur {player}")
        Afficher()
        ligne=int(input("taper le numero de ligne: "))
        colone=int(input("taper le numero de colone: "))
        while ligne>3  or colone>3 :
           ligne=int(input("Attention!! vueillez taper le numero de ligne entre 1 et 3: "))
           colone=int(input("Attention!! vueillez taper le numero de colone entre 1 et 3: "))
        #la methode fixe:
        ligne_colone_fix(ligne,colone,player)
        #vérifier si le joueur actuel est gagné ou non:
        if gagné(tab,player):
            print(f"le joueur {player} gagne le jeu!")
            break
        # vérifier si le tab.. est nul ou non:
        if virefier(tab):
            print("Match fini!")
            break
        
        # échange de tour:
        player=joueur(player)
    # la vue finale du tableau.
    print()
    Afficher()
    
#démarrer le jeu:
demarrer()