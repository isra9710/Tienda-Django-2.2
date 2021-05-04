from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
"""AbstractUser
username
firstname
last_name
email
password
groups
user_permissions
is_staff
is_Active
is_superuser
last_login
date_joined
"""

"""AbstractBaseUser
id
password
last_login

"""

#AbstractUser
class User(AbstractUser):
    
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


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
    