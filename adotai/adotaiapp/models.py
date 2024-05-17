from django.db import models

# Create your models here.
class pet(models.Model):
    Img = models.ImageField(upload_to="djangouploads/files/covers")
    Nome = models.CharField(max_length=100)
    Idade = models.IntegerField()
    Caracteristicas = models.CharField(max_length=255)
    def __str__(self):
        return self.Nome