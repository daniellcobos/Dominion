from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
# Create your models here.
class User(AbstractUser):

    Pais = models.CharField(max_length=50, default="Swazilandia")
    Telefono= models.CharField(max_length=15)
    username = models.CharField(max_length=20, unique=True)
 
    def __str__(self):
        return str(self.username)

class Dominio(models.Model):
    Owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'owner')
    Associates = models.ManyToManyField(User,related_name='associates')
    Direction = models.CharField(max_length=50, unique=True)
    Expirationdate= models.DateField(("Date"), default=date.today)
    Expired =models.BooleanField(default=False)

class pedro(models.Model):
    Direction = models.CharField(max_length=50, unique=True)