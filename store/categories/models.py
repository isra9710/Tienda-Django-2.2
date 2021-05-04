from django.db import models
from products.models import Product
# Create your models here.
class Category(models.Model):
    products = models.ManyToManyField(Product, blank=True) 
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
   
    
    def __str__(self):
        return self.title