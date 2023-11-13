from django.db import models

# Create your models here.
class customer_data(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    

class customer_register(models.Model):
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
