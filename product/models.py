from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.TextField(max_length=50)
    unit_price = models.FloatField(max_length=6)