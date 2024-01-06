class Student:

    def __init__(self, nom, prenom, numero_etudiant):
        self._nom = nom
        self._prenom = prenom
        self._numero_etudiant = numero_etudiant
        self._credits = 0

    def add_credits(self, nombre_credits):
        if nombre_credits <= 0:
            raise ValueError("Le nombre de crédits doit être supérieur à 0")
        self._credits += nombre_credits

    def studentEval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    @property
    def level(self):
        return self.studentEval()

    def studentInfo(self):
        print(f"Nom = {self._nom}  Prénom = {self._prenom}  id = {self._numero_etudiant}  Niveau = {self.level}")


etudiant = Student("John", "Doe", 145)

for i in range(3):
    etudiant.add_credits(24)

etudiant.studentInfo()
