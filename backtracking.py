import copy
import time

tps1 = time.time()
solution_found = False

def genMap(size):
    """
    Génère un tableau représentant un échiquier.
    """
    return [[0 for _ in range(size)] for _ in range(size)]

# Liste des possibilités accessibles depuis une case sous forme de fonction
posibiliteF = [
    lambda x, y: [x+2, y+1],
    lambda x, y: [x+2, y-1],
    lambda x, y: [x-2, y+1],
    lambda x, y: [x-2, y-1],
    lambda x, y: [x+1, y+2],
    lambda x, y: [x-1, y+2],
    lambda x, y: [x+1, y-2],
    lambda x, y: [x-1, y-2],
]

def display(board):
    """
    Affiche un échiquier à partir d'un tableau.
    """
    return "\n".join(" ".join(str(cell) for cell in row) for row in board)

def countCase(board):
    """
    Compte le nombre de cases parcourues dans un chemin.
    """
    return sum(cell >= 1 for row in board for cell in row)

def cavalier(pos, board, n, taille=5, chemin=[]):
    global solution_found, tps1

    if solution_found:
        return

    tmpBoard = copy.deepcopy(board)
    tmpChemin = chemin.copy()

    tmpBoard[pos[1]][pos[0]] = n + 1
    tmpChemin.append(pos)

    if n == taille * taille - 1:
        solution_found = True
        print(display(tmpBoard))
        print(tmpChemin)
        tps2 = time.time()
        print("Temp écouler: ", tps2 - tps1, "seconds")
        return

    for case in (p(pos[0], pos[1]) for p in posibiliteF):
        x2, y2 = case
        if 0 <= x2 < taille and 0 <= y2 < taille and tmpBoard[y2][x2] == 0:
            cavalier([x2, y2], tmpBoard, n + 1, taille, tmpChemin)

intTaille = 5  # Taille de l'échiquier
cavalier([2, 2], genMap(intTaille), 0, intTaille, [])
