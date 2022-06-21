from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    