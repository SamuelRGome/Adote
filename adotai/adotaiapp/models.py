from django.db import models

# Create your models here.
class pet(models.Model):
    Img = models.ImageField(null= True, blank= True, upload_to="Img_pet/")
    Nome = models.CharField(max_length=100)
    Idade = models.IntegerField()
    Caracteristicas = models.CharField(max_length=255)