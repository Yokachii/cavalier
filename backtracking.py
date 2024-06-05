import copy

def genMap(int):
    """
    Génére un tableau de tableau correspondent a un echecier
    """
    array = []
    for i in range(int):
        array.append([])
        for j in range(int):
            array[i].append(0)
    return array

# Liste des posibiliée accesible depuis une case sous forme de fonction
posibiliteF = [
    lambda x, y: [x+2,y+1],
    lambda x, y: [x+2,y-1],
    lambda x, y: [x-2,y+1],
    lambda x, y: [x-2,y-1],
    lambda x, y: [x+1,y+2],
    lambda x, y: [x-1,y+2],
    lambda x, y: [x+1,y-2],
    lambda x, y: [x-1,y-2],
]

def display(map):
    """
    Permet d'afficher un echecier a partir d'un tableau
    """
    text = ""
    for i in range(len(map)):
        text+="\n"
        for j in range(len(map[0])):
            text+=str(map[i][j])+" "
    return text
        
def countCase(map):
    """
    Permet de compter le nombre de case parcourie dans un chemain
    """
    c = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j]>=1:
                c += 1
    return c

def cavalier(pos,map,n,taille=5,chemain=[]):
    """
    Fonction de backtracking cherchant des solution au problème
    """

    tmpN = n
    tmpMap = copy.deepcopy(map)
    tmpChemain = copy.deepcopy(chemain)

    tmpMap[pos[1]][pos[0]]=n+1
    tmpChemain.append(pos)
    

    if n>25 :
        return
    
    tmpA = False
    for case in [p(pos[0], pos[1]) for p in posibiliteF] :

        x2 = case[0]
        y2 = case[1]

        if x2<=taille-1 and y2 <=taille-1 and x2 >=0 and y2 >=0:


            if tmpMap[y2][x2] <1:
                tmpA=True
                cavalier([x2,y2],tmpMap,tmpN+1,taille,tmpChemain)
                
    if tmpA == False :
        if n>=taille*taille-1 :
            print(display(tmpMap))
            print(chemain)
    
cavalier([2,2],genMap(5),0,5,[])