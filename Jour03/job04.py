class Joueur:

    def __init__(self, nom, numero, position, nb_buts=0, nb_passes_decisives=0,
                 nb_cartons_jaunes=0, nb_cartons_rouges=0):
        self._nom = nom
        self._numero = numero
        self._position = position
        self._nb_buts = nb_buts
        self._nb_passes_decisives = nb_passes_decisives
        self._nb_cartons_jaunes = nb_cartons_jaunes
        self._nb_cartons_rouges = nb_cartons_rouges

    def marquerUnBut(self):
        self._nb_buts += 1

    def effectuerUnePasseDecisive(self):
        self._nb_passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self._nb_cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self._nb_cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Nom : {self._nom}")
        print(f"Numéro : {self._numero}")
        print(f"Position : {self._position}")
        print(f"Nombre de buts marqués : {self._nb_buts}")
        print(f"Nombre de passes décisives effectuées : {self._nb_passes_decisives}")
        print(f"Nombre de cartons jaunes reçus : {self._nb_cartons_jaunes}")
        print(f"Nombre de cartons rouges reçus : {self._nb_cartons_rouges}")


class Equipe:

    def __init__(self, nom, joueurs):
        self._nom = nom
        self._joueurs = joueurs

    def ajouterJoueur(self, joueur):
        self._joueurs.append(joueur)

    def afficherStatsJoueurs(self):
        for joueur in self._joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, numero, statistique, valeur):
        for joueur in self._joueurs:
            if joueur._numero == numero:
                if statistique == "buts":
                    joueur._nb_buts += valeur
                elif statistique == "passes_decisives":
                    joueur._nb_passes_decisives += valeur
                elif statistique == "cartons_jaunes":
                    joueur._nb_cartons_jaunes += valeur
                elif statistique == "cartons_rouges":
                    joueur._nb_cartons_rouges += valeur


joueur1 = Joueur("Lionel Messi", 10, "Attaquant", 700, 300, 20, 5)
joueur2 = Joueur("Cristiano Ronaldo", 7, "Attaquant", 800, 250, 30, 10)
joueur3 = Joueur("Neymar", 11, "Attaquant", 600, 200, 15, 2)

equipe1 = Equipe("FC Barcelone", [joueur1, joueur2, joueur3])

equipe1.afficherStatsJoueurs()

# Simuler un match
equipe1.mettreAJourStatistiquesJoueur(10, "buts", 1)
equipe1.mettreAJourStatistiquesJoueur(11, "passes_decisives", 2)
equipe1.mettreAJourStatistiquesJoueur(7, "cartons_jaunes", 1)

equipe1.afficherStatsJoueurs()
