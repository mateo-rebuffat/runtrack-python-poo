import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.subir_degats(degats)
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

    def subir_degats(self, degats):
        self.vie -= degats
        if self.vie < 0:
            self.vie = 0
        print(f"{self.nom} subit {degats} points de dégâts. Vie restante : {self.vie}")

class Jeu:
    def __init__(self):
        self.joueur = None
        self.ennemi = None
        self.niveau = None

    def choisirNiveau(self):
        niveaux = {'facile': 80, 'normal': 60, 'difficile': 40}
        print("Choisissez le niveau de difficulté (facile, normal, difficile) : ")
        while True:
            choix = input().lower()
            if choix in niveaux:
                self.niveau = choix
                break
            else:
                print("Veuillez choisir une difficulté valide.")

    def lancerJeu(self):
        niveaux_vie = {'facile': 80, 'normal': 60, 'difficile': 40}

        vie_joueur = 100
        vie_ennemi = niveaux_vie[self.niveau]

        nom_joueur = input("Entrez le nom de votre personnage : ")
        self.joueur = Personnage(nom_joueur, vie_joueur)
        self.ennemi = Personnage("Ennemi", vie_ennemi)

        print(f"\nBienvenue, {nom_joueur} ! Préparez-vous à combattre l'ennemi au niveau {self.niveau}.")
        print("Que le combat commence!\n")

        while self.joueur.vie > 0 and self.ennemi.vie > 0:
            self.tour_de_jeu()
            self.afficher_etat()
            self.verifierSante()

        self.verifierGagnant()

    def tour_de_jeu(self):
        self.joueur.attaquer(self.ennemi)
        if self.ennemi.vie > 0:
            self.ennemi.attaquer(self.joueur)

    def afficher_etat(self):
        print(f"\nÉtat du jeu :")
        print(f"{self.joueur.nom} - Vie : {self.joueur.vie}")
        print(f"{self.ennemi.nom} - Vie : {self.ennemi.vie}")

    def verifierSante(self):
        if self.joueur.vie <= 0:
            print(f"\n{self.joueur.nom} n'a plus de vie. Vous avez perdu.")
        elif self.ennemi.vie <= 0:
            print(f"\nL'ennemi n'a plus de vie. Vous avez gagné.")

    def verifierGagnant(self):
        if self.joueur.vie > 0:
            print("\nFélicitations ! Vous avez vaincu l'ennemi.")
        elif self.ennemi.vie > 0:
            print("\nVous avez perdu. L'ennemi a vaincu.")

# Exemple d'utilisation
jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()
