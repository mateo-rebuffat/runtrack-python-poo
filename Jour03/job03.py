class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} ({self.statut})"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [t for t in self.taches if t.titre != titre]

    def marquerCommeFinie(self, titre):
        for t in self.taches:
            if t.titre == titre:
                t.statut = "Terminée"
                break

    def afficherListe(self):
        return [str(t) for t in self.taches]

    def filterListe(self, statut):
        return [str(t) for t in self.taches if t.statut == statut]


# Exemple d'utilisation
tache1 = Tache("Faire les courses", "Acheter des légumes et du lait")
tache2 = Tache("Réviser pour l'examen", "Relire les chapitres 1 à 3", "À faire")
tache3 = Tache("Faire du sport", "Jogging au parc")

liste_taches = ListeDeTaches()

# Ajouter des tâches à la liste
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

# Afficher la liste initiale
print("Liste initiale:")
print(liste_taches.afficherListe())

# Marquer une tâche comme terminée
liste_taches.marquerCommeFinie("Réviser pour l'examen")

# Supprimer une tâche
liste_taches.supprimerTache("Faire du sport")

# Afficher la liste mise à jour
print("\nListe mise à jour:")
print(liste_taches.afficherListe())

# Afficher les tâches à faire
print("\nTâches à faire:")
print(liste_taches.filterListe("À faire"))
