class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    # Assesseurs (getters)
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    # Mutateurs (setters)
    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def set_reservoir(self, nouveau_reservoir):
        self.__reservoir = nouveau_reservoir

    # Méthode privée pour vérifier le niveau du réservoir
    def __verifier_plein(self):
        return self.__reservoir > 5

    # Méthode pour démarrer la voiture
    def demarrer(self):
        if self.__verifier_plein():
            self.set_en_marche(True)
            print("La voiture démarre.")
        else:
            print("Erreur : Niveau de carburant trop bas. La voiture ne peut pas démarrer.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        self.set_en_marche(False)
        print("La voiture s'arrête.")

# Exemple d'utilisation
ma_voiture = Voiture("Toyota", "Camry", 2020, 30000)

# Affichage des valeurs initiales
print("Marque:", ma_voiture.get_marque())
print("Modèle:", ma_voiture.get_modele())
print("Année:", ma_voiture.get_annee())
print("Kilométrage:", ma_voiture.get_kilometrage())
print("En marche:", ma_voiture.get_en_marche())
print("Niveau de réservoir:", ma_voiture.get_reservoir())

# Démarrage de la voiture
ma_voiture.demarrer()

# Arrêt de la voiture
ma_voiture.arreter()

# Modification des valeurs
ma_voiture.set_kilometrage(35000)
ma_voiture.set_reservoir(20)

# Affichage des valeurs après les modifications
print("\nNouveau kilométrage:", ma_voiture.get_kilometrage())
print("Nouveau niveau de réservoir:", ma_voiture.get_reservoir())
