from os import name
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Term(models.Model):
    name = models.CharField(max_length=255)

class Paymenttype(models.Model):
    name = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    sku = models.CharField(max_length=255)
    ispublic = models.BooleanField()

class Priceplan(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=CASCADE)
    term = models.ForeignKey(Term, on_delete=CASCADE)    

class Priceplandetail(models.Model):
    priceplan = models.ForeignKey(Priceplan, on_delete=CASCADE)
    description = models.CharField(max_length=255)
    paymenttype = models.ForeignKey(Paymenttype, on_delete=CASCADE)
    amount = models.IntegerField()