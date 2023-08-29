from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    views = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
    
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    views = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/' , blank=True , null=True)
    
    category = models.ManyToManyField(Category)