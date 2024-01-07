import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        self.creer_paquet()

    def creer_paquet(self):
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']

        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        if not self.paquet:
            print("Le paquet est vide.")
            return None
        return self.paquet.pop()

class Blackjack:
    def __init__(self):
        self.jeu = Jeu()
        self.mains_joueur = []
        self.main_croupier = []

    def distribuer_cartes(self):
        self.jeu.melanger_paquet()
        self.mains_joueur = [self.jeu.tirer_carte(), self.jeu.tirer_carte()]
        self.main_croupier = [self.jeu.tirer_carte(), self.jeu.tirer_carte()]

    def afficher_mains(self, reveler_croupier=False):
        print("Main du joueur:")
        for carte in self.mains_joueur:
            print(f"{carte.valeur} de {carte.couleur}")
        print("\nMain du croupier:")
        for carte in self.main_croupier:
            if reveler_croupier:
                print(f"{carte.valeur} de {carte.couleur}")
            else:
                print("Carte cachée")
                reveler_croupier = True

    def calculer_points(self, main):
        total = 0
        as_count = 0

        for carte in main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                total += 10
            elif carte.valeur == 'As':
                total += 11
                as_count += 1
            else:
                total += int(carte.valeur)

        while total > 21 and as_count:
            total -= 10
            as_count -= 1

        return total

    def joueur_tirer_carte(self):
        carte = self.jeu.tirer_carte()
        if carte:
            self.mains_joueur.append(carte)

    def jouer(self):
        self.distribuer_cartes()
        self.afficher_mains()

        while True:
            choix = input("Voulez-vous tirer une carte ? (Oui/Non): ").lower()
            if choix == 'oui':
                self.joueur_tirer_carte()
                self.afficher_mains()

                if self.calculer_points(self.mains_joueur) > 21:
                    print("Vous avez dépassé 21. Vous avez perdu.")
                    return
            elif choix == 'non':
                break
            else:
                print("Veuillez saisir 'Oui' ou 'Non'.")

        while self.calculer_points(self.main_croupier) < 17:
            self.main_croupier.append(self.jeu.tirer_carte())

        self.afficher_mains(reveler_croupier=True)

        points_joueur = self.calculer_points(self.mains_joueur)
        points_croupier = self.calculer_points(self.main_croupier)

        if points_joueur > 21:
            print("Vous avez dépassé 21. Vous avez perdu.")
        elif points_croupier > 21 or points_joueur > points_croupier:
            print("Vous avez gagné !")
        elif points_joueur == points_croupier:
            print("Match nul.")
        else:
            print("Le croupier a gagné.")

# Exemple d'utilisation
blackjack = Blackjack()
blackjack.jouer()
