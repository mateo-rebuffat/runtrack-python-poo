class Animal:

    def __init__(self, age=0, prenom=""):
        self.age = age
        self.prenom = prenom

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom


animal = Animal()
print("L'age de l'animal", animal.age, "ans")
animal.vieillir()
print("L'age de l'animal", animal.age, "ans")

animal.nommer("Luna")
print("L'animal se nomme", animal.prenom)
