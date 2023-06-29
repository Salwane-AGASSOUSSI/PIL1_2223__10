from django.db import models



class etudiant(models.Model):
    matricule = models.CharField(max_length=50)
    nom_prenoms=models.CharField(max_length=100)
    sexe = models.CharField(max_length=50)
    Telephone = models.CharField(max_length=50)

    

    

    # Ajoutez d'autres champs si nécessaire

    def __str__(self):
        return self.nom_prenoms


    # Ajoutez d'autres méthodes ou propriétés personnalisées si nécessaire
class key(models.Model):
    cle=models.CharField(max_length=4)
