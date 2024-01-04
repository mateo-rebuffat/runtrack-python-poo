import math

class Produit:

    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + (self.TVA / 100))

    def afficher(self):
        print(f"Nom : {self.nom}")
        print(f"Prix HT : {self.prixHT}")
        print(f"TVA : {self.TVA}")
        print(f"Prix TTC : {self.CalculerPrixTTC()}")

    def modifierNom(self, nom):
        self.nom = nom

    def modifierPrixHT(self, prixHT):
        self.prixHT = prixHT

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

    def getPrixTTC(self):
        return self.CalculerPrixTTC()


produit1 = Produit("Playstation", 1000, 20)
produit2 = Produit("Téléphone", 500, 19.6)

produit1.afficher()
produit2.afficher()

produit1.modifierNom("PC portable")
produit1.modifierPrixHT(1200)

produit1.afficher()
produit2.afficher()