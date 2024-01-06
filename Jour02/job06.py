class Commande:

    def __init__(self, numero_commande):
        self._numero_commande = numero_commande
        self._plats_commandes = []
        self._statut = "en cours"

    def ajouter_plat(self, nom_plat, prix):
        plat = {
            "nom": nom_plat,
            "prix": prix,
            "statut": self._statut,
        }
        self._plats_commandes.append(plat)

    def annuler(self):
        self._statut = "annulée"

    @property
    def total(self):
        return sum(plat["prix"] for plat in self._plats_commandes)

    def afficher(self):
        print(f"Numéro de commande : {self._numero_commande}")
        print("Plats commandés :")
        for plat in self._plats_commandes:
            print(f"    Nom : {plat['nom']}")
            print(f"    Prix : {plat['prix']}")
            print(f"    Statut : {plat['statut']}")
            print(f"Total : {self.total + self.calculer_tva()}")


    def calculer_tva(self, taux_tva=0.2):
        return self.total * taux_tva



commande = Commande(12345)
commande.ajouter_plat("Pizza", 15)
commande.ajouter_plat("Coupe de glace", 5)

commande.afficher()

# Le résultat est le suivant :

# Numéro de commande : 12345
# Plats commandés :
#    Nom : Pizza
#    Prix : 15
#    Statut : en cours
#    Nom : Coupe de glace
#    Prix : 5
#    Statut : en cours
# Total : 20
