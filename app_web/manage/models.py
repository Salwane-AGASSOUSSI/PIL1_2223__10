from django.db import models


class EmploiTemps(models.Model):
    specialite = models.CharField(max_length=100)
    niveau_etude = models.CharField(max_length=100)
    semaine = models.CharField(max_length=100)
    jour = models.CharField(max_length=100)
    intitule_cours = models.CharField(max_length=100)
    nom_professeur = models.CharField(max_length=100)
    materiel_necessaire = models.CharField(max_length=100)
    creneau_horaire = models.CharField(max_length=100)
    infos_supplementaires = models.CharField(max_length=100)



class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    matricule = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

