from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta, date

# Create your models here.
class Etudiant(AbstractUser):
    departement = models.CharField(max_length=100)
    filiere = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.username} ({self.filiere})"
    
class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    image = models.ImageField(upload_to='livres/', null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titre} - {self.auteur}"

class Emprunt(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour = models.DateField()
    rendu = models.BooleanField(default=False)

    def est_retard(self):
        return not self.rendu and date.today() > self.date_retour

    def save(self, *args, **kwargs):
        # Si date_retour n'est pas définie, on ajoute 14 jours par défaut
        if not self.date_retour:
            self.date_retour = self.date_emprunt + timedelta(days=14)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.livre.titre} emprunté par {self.etudiant.username}"

class Notification(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    lue = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification pour {self.etudiant.username} - {self.message[:30]}"
