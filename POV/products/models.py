from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100)
    
    def __str__(self):

        return self.name
    
    
    
class Product(models.Model):

    image = models.ImageField(upload_to='media/', default='default.png')
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category , on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    instock_Qty = models.IntegerField(default=0) 
    description = models.TextField(max_length=100)
    custom = models.BooleanField(default=False)
    
    def __str__(self):

        return self.title
    
    def get_absolute_url(self):

        return reverse('product:detail', kwargs={'pk':self.pk})


