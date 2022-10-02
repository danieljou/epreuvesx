from django.db import models

# Create your models here.


class Matiere(models.Model):

    Nom_de_la_matiere = models.CharField(max_length=50)
    def __str__(self):
        return self.Nom_de_la_matiere

    def get_absolute_url(self):
        return reverse("Matiere_detail", kwargs={"pk": self.pk})

class Exercice(models.Model):

    matiere = models.ForeignKey("Matiere",  on_delete=models.SET_NULL, null = True)
    Titre = models.CharField(max_length=50)
    Enonce = models.TextField('Enoncé')
    Question = models.TextField('Questions')
    Auteur = models.ForeignKey("users.User", on_delete=models.SET_NULL, null = True)
    
    def __str__(self):
        return self.Titre


class Epreuve(models.Model):

    Titre = models.CharField( max_length=50, unique = True)
    Nombre_exerce = models.PositiveIntegerField('Nombre d\'exercice')
    matiere = models.ForeignKey("Matiere", on_delete=models.CASCADE)
    exercices = models.ManyToManyField("Exercice")
    def __str__(self):
        return self.Titre

    

   
