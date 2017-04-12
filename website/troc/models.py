from django.db import models

"""
class Annonce(models.Model):
    Titre = models.CharField(max_length=30)
    Categorie = models.CharField(max_length=30)
    Localisation=models.ForeignKey(Localisation, on_delete=models.CASCADE)
    Image = models.CharField(max_length=30)
    Prix = models.CharField(max_length=30)
    Posteur=models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateField()
    Etat=models.IntergerField()



class Localisation(models.Model):
    Pays = models.CharField(max_length=30)
    Region = models.CharField(max_length=30)
    Departement = models.CharField(max_length=30)
    Ville = models.CharField(max_length=30)
    CP=

class Pays(models.Model):
    COUNTRY=(
        ('FR','France')
    )
    Pays = models.CharField(max_length=30,choices=COUNTRY)

class Region(models.Model):
    REGION=(
        ('France')
    )
    Pays = models.CharField(max_length=30,choices=REGION)

class Departement(models.Model):
    DEPART=(
        ('FR','France')
    )
    Pays = models.CharField(max_length=30,choices=DEPART)

class Ville(models.Model):
    CITY=(
        ('France')
    )
    Pays = models.CharField(max_length=30,choices=CITY)


class CP(models.Model):
    POSTAL=(
        ('France')
    )
     = models.IntegerField(choices=CITY)
"""
