class CompteBancaire:

    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self._numero_compte = numero_compte
        self._nom = nom
        self._prenom = prenom
        self._solde = solde
        self._decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte : {self._numero_compte}")
        print(f"Nom : {self._nom}")
        print(f"Prénom : {self._prenom}")
        print(f"Solde : {self._solde}")

    def afficherSolde(self):
        print(f"Solde : {self._solde}")

    def versement(self, montant):
        self._solde += montant
        print(f"Le nouveau solde est de {self._solde}")

    def retrait(self, montant):
        if self._solde < montant:
            if self._decouvert:
                self._solde -= montant
                print(f"Le nouveau solde est de {self._solde}")
            else:
                print(f"Solde insuffisant")
        else:
            self._solde -= montant
            print(f"Le nouveau solde est de {self._solde}")

    def agios(self):
        if self._solde < 0:
            agios = 0.05 * self._solde
            self._solde += agios
            print(f"Agios appliqués : {agios}")

    def virement(self, reference, compte_beneficiaire, montant):
        if self._solde >= montant:
            self._solde -= montant
            compte_beneficiaire._solde += montant
            print(f"Virement effectué avec succès ({reference})")
        else:
            print(f"Solde insuffisant")


compte1 = CompteBancaire(123456789, "Dupont", "Jean", 1000)
compte1.afficher()
compte1.versement(500)
compte1.afficher()
compte1.retrait(100)
compte1.afficher()

compte2 = CompteBancaire(987654321, "Martin", "Marie", -100, decouvert=True)
compte2.afficher()

compte1.virement("1234", compte2, 500)
compte1.afficher()
compte2.afficher()
