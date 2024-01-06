class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nom(self):
        return self.__nom

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def augmenter_population(self):
        self.__nombre_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        ville.augmenter_population()  # Appel de la méthode de la classe Ville pour augmenter la population

    def ajouter_population(self):
        self.__ville.augmenter_population()

# Création d'un objet Ville avec comme arguments “Paris” et 1000000
paris = Ville("Paris", 1000000)
# Affichage en console du nombre d’habitants de la ville de Paris
print(f"Population de la ville de {paris.get_nom()}: {paris.get_nombre_habitants()}")

# Création d'un autre objet Ville avec comme arguments “Marseille” et 861635
marseille = Ville("Marseille", 861635)
# Affichage en console du nombre d’habitants de la ville de Marseille
print(f"Population de la ville de {marseille.get_nom()}: {marseille.get_nombre_habitants()}")

# Création des objets Personne
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Affichage du nombre d’habitants après l’arrivée de ces nouvelles personnes
print(f"Mise à jour de la population de la ville de {paris.get_nom()} {paris.get_nombre_habitants()} habitants")
print(f"Mise à jour de la population de la ville de {marseille.get_nom()} {marseille.get_nombre_habitants()} habitants") 
