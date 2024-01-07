class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def getLongueur(self):
        return self.__longueur

    def setLongueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def getLargeur(self):
        return self.__largeur

    def setLargeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def getHauteur(self):
        return self.__hauteur

    def setHauteur(self, nouvelle_hauteur):
        self.__hauteur = nouvelle_hauteur

    def volume(self):
        return self.getLongueur() * self.getLargeur() * self.__hauteur



# Instanciation de la classe Rectangle
rectangle = Rectangle(longueur=5, largeur=3)
print(f"Longueur : {rectangle.getLongueur()}, Largeur : {rectangle.getLargeur()}")
print(f"Périmètre : {rectangle.perimetre()}")
print(f"Surface : {rectangle.surface()}")

# Instanciation de la classe Parallelepipede
parallelepipede = Parallelepipede(longueur=5, largeur=6, hauteur=8)
print(f"Longueur : {parallelepipede.getLongueur()}, Largeur : {parallelepipede.getLargeur()}, Hauteur : {parallelepipede.getHauteur()}")
print(f"Périmètre : {parallelepipede.perimetre()}")
print(f"Surface : {parallelepipede.surface()}")
print(f"Volume : {parallelepipede.volume()}")
