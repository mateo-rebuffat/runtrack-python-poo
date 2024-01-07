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


# Instanciation d'une Personne et d'un Eleve
une_personne = Personne()
une_personne.afficherAge()  # Affiche : L'âge de la personne est 14 ans.
une_personne.bonjour()      # Affiche : Hello

un_eleve = Eleve()
un_eleve.afficherAge()      # Affiche : J'ai 14 ans.
un_eleve.allerEnCours()     # Affiche : Je vais en cours.

professeur = Professeur(matiereEnseignee="Mathématiques")
print(f"Matière enseignée : {professeur.getMatiereEnseignee()}")
professeur.enseigner()  # Affiche : Le cours va commencer.