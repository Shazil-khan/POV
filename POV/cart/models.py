from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Cart(models.Model): 

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products  = models.ManyToManyField(Product)


    def total(self):
        total = 0
        for product in self.products.all():
            total += product.price
        print(total)
        return total


