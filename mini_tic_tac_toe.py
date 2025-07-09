def afficher_plateau(plateau):
    print("\n")
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-"*10)

def verifier_gagnant(plateau, joueur):
    for i in range(3):
        if all([case == joueur for case in plateau[i]]) or all([plateau[j][i] == joueur for j in range(3)]):
            return True
        if plateau[0][0] == plateau[1][1] == plateau[2][2] == joueur or plateau[0][2] == plateau[1][1] == plateau[2][0] == joueur:
            return True
    return False

def main():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueur = "X"

    for tour in range(9):
        afficher_plateau(plateau)
        print(f"Tour du joueur {joueur}")

        try:
            ligne = int(input("Choisis la ligne (0,1,2) : "))
            col = int(input("Choisis la colonne (0,1, 2) : "))
        except ValueError:
            print("Entrée invalide, essaie encore.")
            continue

        if 0 <= ligne < 3 and 0 <= col < 3 and plateau[ligne][col] == " ":
            plateau[ligne][col] = joueur
            if verifier_gagnant(plateau, joueur):
                afficher_plateau(plateau)
                print(f"Le joueur {joueur} a gagné!")
                return
            joueur = "O" if joueur == "X" else "X"
        else:
            print("Case occupé ou invalide, essaie encore.")

    afficher_plateau(plateau)
    print("Match null!")

if __name__ == "__main__":
    main()