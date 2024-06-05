import copy

def genMap(width):
    """
    Génère un tableau représentant un echecier
    """
    array = []
    for i in range(width):
        array.append([])
        for j in range(width):
            array[i].append(0)
    return array

def listePoidCaseFonction(width) :
    """
    Génère le même tableau que la fonction 'genMap' mais en incluant
    le nombre de case attaignable depuis chaque case
    Génère un tableau représentant un echecier dans le quelle chaque case est représenter par sont poid
    """
    array = []
    for i in range(width):
        array.append([])
        for j in range(width):
            tmpInt = 0
            for case in [p(j,i) for p in ListePossibilitee] :
                x2 = case[0]
                y2 = case[1]
                if x2<=width-1 and y2 <=width-1 and x2 >=0 and y2 >=0:
                    tmpInt+=1
            array[i].append(tmpInt)
    return array

ListePossibilitee = [
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
    Renvoie une chaine de caractère pour afficher le tableau avec les deplacement de manière lisible
    """
    text = ""
    for i in range(len(map)):
        text+="\n"
        for j in range(len(map[0])):
            text+=str(map[i][j])+" "
    return text


def rosace_heuristique(pos,map,n,taille=5,chemain=[]):

    tmpN = 0
    tmpN = n
    tmpMap = copy.deepcopy(map)
    tmpChem = copy.deepcopy(chemain)

    tmpMap[pos[1]][pos[0]]=n+1
    tmpChem.append(pos)

    meilleurCases = []
    meilleurCaseNb = 8

    
    for case in [p(pos[0], pos[1]) for p in ListePossibilitee] :
        x2 = case[0]
        y2 = case[1]
        if x2<=taille-1 and y2 <=taille-1 and x2 >=0 and y2 >=0:
            """
            Vérifier si la case est sur l'échecier puis stocker les case avec le moin 
            de possibilitée dans un tableau
            """

            if tmpMap[y2][x2] <1 :
                if listePoidCaseFonction(taille)[y2][x2] < meilleurCaseNb :
                    meilleurCases = [case]
                    meilleurCaseNb=listePoidCaseFonction(taille)[y2][x2]
                if listePoidCaseFonction(taille)[y2][x2] == meilleurCaseNb :
                    meilleurCases.append(case)
                    meilleurCaseNb=listePoidCaseFonction(taille)[y2][x2]
    if len(tmpChem) >= taille*taille :
        """
        Si le nombre de case parcourue est au moin égale au nombre de case de l'échecier
        On affiche le chemain emprunter
        """
        print(display(tmpMap))
        print(tmpChem)
    
    if len(meilleurCases) >= 1 :
        tmpA = True
        for uneCase in meilleurCases :
            rosace_heuristique(uneCase,tmpMap,tmpN+1,taille,tmpChem)
            
    
intTaille = 5 # Taille de l'échecier


rosace_heuristique([2,2],genMap(intTaille),0,intTaille)