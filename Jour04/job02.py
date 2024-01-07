class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"L'âge de la personne est {self.age} ans.")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans.")


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=14):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer.")

     # Méthode pour accéder à la matière enseignée (getter)
    def getMatiereEnseignee(self):
        return self.__matiereEnseignee

    # Méthode pour modifier la matière enseignée (setter)
    def setMatiereEnseignee(self, nouvelle_matiere):
        self.__matiereEnseignee = nouvelle_matiere


# Instanciation d'un Eleve
un_eleve = Eleve()

# Faire dire bonjour à l'élève
un_eleve.bonjour()

# Faire dire à l'élève qu'il va en cours
un_eleve.allerEnCours()

# Redéfinir l'âge de l'élève à 15 ans
un_eleve.modifierAge (15)

# Afficher le nouvel âge de l'élève
un_eleve.afficherAge()

# Instanciation d'un Professeur
professeur = Professeur(matiereEnseignee="Mathématiques", age=40)

# Faire dire bonjour au professeur
professeur.bonjour()

# Faire commencer le cours au professeur
professeur.enseigner()
