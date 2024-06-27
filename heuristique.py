import copy
import time

tps1 = time.time()
tmpaa = False

def genMap(width):
    """
    Génère un tableau représentant un échiquier
    """
    return [[0 for _ in range(width)] for _ in range(width)]

def listePoidCaseFonction(width, ListePossibilitee):
    """
    Génère un tableau représentant un échiquier dans lequel chaque case est représentée par son poids,
    c'est-à-dire le nombre de cases atteignables depuis chaque case.
    """
    array = []
    for i in range(width):
        row = []
        for j in range(width):
            tmpInt = 0
            for case in [p(j,i) for p in ListePossibilitee]:
                x2, y2 = case
                if 0 <= x2 < width and 0 <= y2 < width:
                    tmpInt += 1
            row.append(tmpInt)
        array.append(row)
    return array

ListePossibilitee = [
    lambda x, y: [x+2, y+1],
    lambda x, y: [x+2, y-1],
    lambda x, y: [x-2, y+1],
    lambda x, y: [x-2, y-1],
    lambda x, y: [x+1, y+2],
    lambda x, y: [x-1, y+2],
    lambda x, y: [x+1, y-2],
    lambda x, y: [x-1, y-2],
]

def display(map):
    """
    Renvoie une chaîne de caractères pour afficher le tableau des déplacements de manière lisible
    """
    text = ""
    for row in map:
        text += "\n" + " ".join(str(cell) for cell in row)
    return text

def rosace_heuristique(pos, map, n, taille=5, chemin=[]):
    global tmpaa

    tmpN = n
    tmpMap = copy.deepcopy(map)
    tmpChemin = copy.deepcopy(chemin)

    tmpMap[pos[1]][pos[0]] = n + 1
    tmpChemin.append(pos)

    meilleurCases = []
    meilleurCaseNb = 8

    poidsCases = listePoidCaseFonction(taille, ListePossibilitee)
    
    for case in [p(pos[0], pos[1]) for p in ListePossibilitee]:
        x2, y2 = case
        if 0 <= x2 < taille and 0 <= y2 < taille:
            if tmpMap[y2][x2] < 1:
                if poidsCases[y2][x2] < meilleurCaseNb:
                    meilleurCases = [case]
                    meilleurCaseNb = poidsCases[y2][x2]
                elif poidsCases[y2][x2] == meilleurCaseNb:
                    meilleurCases.append(case)

    if len(tmpChemin) >= taille * taille:
        if not tmpaa:
            print(display(tmpMap))
            print(tmpChemin)
            tps2 = time.time()
            print(tps2 - tps1)
            tmpaa = True
    
    if meilleurCases:
        for uneCase in meilleurCases:
            rosace_heuristique(uneCase, tmpMap, tmpN + 1, taille, tmpChemin)

intTaille = 5  # Taille de l'échiquier
rosace_heuristique([2, 2], genMap(intTaille), 0, intTaille)
