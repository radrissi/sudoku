#main system
import sys



# Traitement des données
def parsing(lines):
    tableau = []
    for line in lines:
        tab = []
        number = 0
        for caractere in line:
            if caractere == "_":
                number = 0
            elif caractere.isdigit():
                number = int(caractere)
            elif caractere == "\n" : 
                break
            else :
                print("Caractere invalide dans la ligne")
                exit()
            tab.append(number)
        if len(tab) !=9:
            print ("Ligne de taille différente")  
            exit()
        tableau.append(tab)
    if len(tableau) !=9:
        print("Trop ou pas assez de lignes")
        exit()
    return tableau

def printTableau(tableau):
    for lines in tableau:
        for number in lines:
            print(number, end="")
        print ()

# Résoudre le jeu

def solve(tableau):
    find = trouver_cellule_vide(tableau)
    if not find:
        return True
    else:
        row, col = find

    for number in range(1,10):
        if valid(tableau, number, (row, col)):
            tableau[row][col] = number

            if solve(tableau):
                return True

            tableau[row][col] = 0

    return False


def valid(tableau, number, position):

    # Vérifier la ligne

    for i in range(0,9):
        if tableau[position[0]][i] == number:
            return False

    # Vérifier la colonne
    for i in range(0,9):
        if tableau[i][position[1]] == number: 
            return False

    # Vérifier dans petit carré 3*3

    tableau_x = position[1] // 3
    tableau_y = position[0] // 3

    for i in range(tableau_y*3, tableau_y*3 + 3):
        for j in range(tableau_x * 3, tableau_x*3 + 3):
            if tableau[i][j] == number:
                return False

    return True

def trouver_cellule_vide(tableau):
    for i in range(0,9):
        for j in range(0,9):
            if tableau[i][j] == 0:
                return (i, j)  

    return None

# Récupération des données
def main():
    args = sys.argv[1:]
    if len(args)==0:
        return
    try:
        f=open(args[0],"r")
        
    except (FileNotFoundError, PermissionError, OSError):
        print("Le fichier n'existe pas ")
        exit()
    else:
        lines = f.readlines() 
        f.close()
    tableau = parsing(lines)
    solve(tableau)
    printTableau(tableau)

if __name__ == '__main__':
    main()



