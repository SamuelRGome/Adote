from django.db import models

# Create your models here.
class pet(models.Model):
    Nome = models.CharField(max_length=100)
    Idade = models.IntegerField(max_length=100)
    Caracteristicas = models.CharField(max_length=255)