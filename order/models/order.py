from django.db import models

from product.models.product import Product

class Order(models.Model):
  product = models.ManyToManyField(Product, blank=False)
  user = models.ForeignKey(User, Null=False)
