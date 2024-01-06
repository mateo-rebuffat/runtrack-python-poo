class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True

    # Assesseurs (getters)
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def get_disponible(self):
        return self.__disponible

    # Mutateurs (setters)
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nb_pages(self, nouveau_nb_pages):
        # Vérification que le nouveau_nb_pages est un entier positif
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif. La valeur n'a pas été modifiée.")

    def set_disponible(self, disponible):
        self.__disponible = disponible

    # Méthode de vérification de la disponibilité du livre
    def verification(self):
        return self.__disponible

    # Méthode pour emprunter le livre
    def emprunter(self):
        if self.verification():
            self.set_disponible(False)
            print("Livre emprunté avec succès.")
        else:
            print("Erreur : Le livre n'est pas disponible pour l'emprunt.")

    # Méthode pour rendre le livre
    def rendre(self):
        if not self.verification():
            self.set_disponible(True)
            print("Livre rendu avec succès.")
        else:
            print("Erreur : Le livre n'a pas été emprunté, impossible de le rendre.")

# Exemple d'utilisation
mon_livre = Livre("Harry Potter", "J.K. Rowling", 400)

# Affichage des valeurs initiales
print("Titre:", mon_livre.get_titre())
print("Auteur:", mon_livre.get_auteur())
print("Nombre de pages:", mon_livre.get_nb_pages())
print("Disponible:", mon_livre.verification())

# Emprunt du livre
mon_livre.emprunter()

# Tentative d'emprunt du livre à nouveau
mon_livre.emprunter()

# Rendu du livre
mon_livre.rendre()

# Tentative de rendu du livre à nouveau
mon_livre.rendre()

# Affichage des valeurs après les modifications
print("\nTitre modifié:", mon_livre.get_titre())
print("Auteur modifié:", mon_livre.get_auteur())
print("Nombre de pages modifié:", mon_livre.get_nb_pages())
print("Disponible:", mon_livre.verification())
