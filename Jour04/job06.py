class Vehicule:
    def __init__(self, marque, modele, annee, prix, portes):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
        self.portes = portes

    def informationsVehicule(self):
        print(f"Marque: {self.marque}\nModèle: {self.modele}\nAnnée: {self.annee}\nPrix: {self.prix}\nNombre de porte: {self.portes}")

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix, portes)

    def informationsVehicule(self):
        super().informationsVehicule()

    def demarrer(self):
        print("Attention, je roule comme un dingue!")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix, portes=None)  # On passe None pour le nombre de portes
        self.roues = roues

    def informationsVehicule(self):
        print(f"Marque: {self.marque}\nModèle: {self.modele}\nAnnée: {self.annee}\nPrix: {self.prix}\nNombre de roue: {self.roues}")

    def demarrer(self):
        print("Vroom,béhbéhbéééééé attention je cabre")

# Instanciation d'un objet Voiture et appel à la méthode demarrer
voiture = Voiture(marque="Mercedes", modele="Classe A", annee=2020, prix=18500, portes=4)
voiture.informationsVehicule()
voiture.demarrer()

# Instanciation d'un objet Moto et appel à la méthode demarrer
moto = Moto(marque="Yamaha", modele="1200 Vmax", annee=1987, prix=4500, roues=2)
moto.informationsVehicule()
moto.demarrer()
