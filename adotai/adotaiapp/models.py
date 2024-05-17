from django.db import models

# Create your models here.
class pet(models.Model):
    Img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    Nome = models.CharField(max_length=100)
    Idade = models.IntegerField()
    Caracteristicas = models.CharField(max_length=255)