from django.db import models
from django.contrib.auth.models import AbstractUser
from orders.common import OrderStatus
# from django.contrib.auth.models import User

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
    
    @property
    def shipping_address(self):
        return self.shippingaddress_set.filter(default=True).first()

    
    def has_shipping_address(self):
        return self.shipping_address is not None
    
    
    def orders_completed(self):
        return self.order_set.filter(status=OrderStatus.COMPLETED).order_by('-id')


    def has_shipping_addresses(self):
        return self.shippingaddress_set.exists()

    @property
    def addresses(self):
        return self.shippingaddress_set.all()

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
    