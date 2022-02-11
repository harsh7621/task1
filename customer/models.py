from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.AutoField
    first_name = models.TextField(max_length=25)
    last_name = models.TextField(max_length=25)
    contact_no = models.TextField(max_length=15)
    pincode = models.IntegerField(default=0)
