import random

def lire_mots(nom_fichier):
    """Lit les mots depuis un fichier texte et retourne une liste."""
    with open(nom_fichier, 'r') as fichier:
        return fichier.read().splitlines()

def afficher_mot(mot, lettres_devinees):
    """Retourne une version du mot avec les lettres devinées ou des _."""

    # Créer une liste vide pour stocker les résultats
    resultat = []

    # Parcourir chaque lettre du mot
    for lettre in mot:
        # Vérifier si la lettre est dans les lettres devinées
        if lettre in lettres_devinees:
            # Ajouter la lettre au résultat
            resultat.append(lettre)
        else:
            # Ajouter un "_" si la lettre n'a pas été devinée
            resultat.append('_')

    # Joindre les éléments de la liste avec un espace entre chaque lettre et retourner le résultat
    return ' '.join(resultat)

def verifier_mot_complet(mot, lettres_devinees):
    """Vérifie si toutes les lettres du mot ont été devinées."""
    for lettre in mot:
        if lettre not in lettres_devinees:
            return False
        else :
            return True

def jeu_du_pendu(nom_fichier):
    """Lance le jeu du pendu."""
    print("le jeu du pendu :")
    mots = lire_mots(nom_fichier)
    if not mots:
        print("Fichier vide ou introuvable.")
        return

    while True:
        mot = random.choice(mots)
        lettres_devinees = ""
        chances = 6

        while chances > 0:
            print(f"\nMot: {afficher_mot(mot, lettres_devinees)}\nChances restantes: {chances}")
            lettre = input("Entrez une lettre: ")

            if lettre in lettres_devinees:
                print("Lettre déjà devinée.")
                continue

            if lettre in mot:
                lettres_devinees += lettre
                print("Bonne lettre!")
            else:
                chances -= 1
                print("Mauvaise lettre...")

            if verifier_mot_complet(mot, lettres_devinees):
                print(f"\nFélicitations! Vous avez trouvé le mot: {mot}")
                break
        else:
            print(f"\nVous avez perdu. Le mot était: {mot}")

        if input("Voulez-vous rejouer ? (o/n): ") != 'o':
            print("Merci d'avoir joué. À bientôt!")
            break


jeu_du_pendu("C:\\Users\\anton\\OneDrive\\Dokumente\\ETS_MONTREAL\\MGA802\\Mot_pendu.txt")
