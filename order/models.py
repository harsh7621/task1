from django.db import models
from customer.models import Customer
from product.models import Product
from datetime import datetime
# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Unit_price = models.FloatField(max_length=6)
    qty = models.IntegerField()
    total_price = models.FloatField(max_length=10)
    date = models.DateTimeField(default=datetime.now())