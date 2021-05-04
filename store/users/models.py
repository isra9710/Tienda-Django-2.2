from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(User):
    class Meta:
        proxy = True
        
    def get_products(self):
        return []

#Si tenemos la necesidad de agregar atributos a nuestro modelo  User, una buena practica es generar una relación 1-1 con un nuevo modelo
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    bio = models.TextField()
    