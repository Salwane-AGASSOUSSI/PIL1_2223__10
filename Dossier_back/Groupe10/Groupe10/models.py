from django.db import models

class Promotion(models.Model):
    nom = models.CharField(max_length=100)

class Enseignement(models.Model):
    nom = models.CharField(max_length=100)

class EmploiTemps(models.Model):
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    enseignement = models.ForeignKey(Enseignement, on_delete=models.CASCADE)
    jour = models.CharField(max_length=20)  # Jour de la semaine (lundi, mardi, etc.)
    heure_debut = models.TimeField()  # Heure de début du cours
    heure_fin = models.TimeField()  # Heure de fin du cours
    salle = models.CharField(max_length=50)  # Salle de cours
    enseignant = models.CharField(max_length=100)  # Nom de l'enseignant
    groupe = models.CharField(max_length=50)  # Groupe d'étudiants
