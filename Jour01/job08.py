import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Cercle de rayon {self.rayon}")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon

# Création de deux cercles avec des rayons différents
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Affichage des informations du cercle 1
cercle1.afficherInfos()
print("Circonférence:", cercle1.circonference())
print("Diamètre:", cercle1.diametre())
print("Aire:", cercle1.aire())
print()

# Affichage des informations du cercle 2
cercle2.afficherInfos()
print("Circonférence:", cercle2.circonference())
print("Diamètre:", cercle2.diametre())
print("Aire:", cercle2.aire())
