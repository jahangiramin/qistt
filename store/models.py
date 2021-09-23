from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Term(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    sku = models.CharField(max_length=255)
    ispublic = models.BooleanField()

    def __str__(self):
        return self.name

class Priceplan(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=CASCADE)
    term = models.ForeignKey(Term, on_delete=CASCADE)
    price = models.IntegerField()
    downpayment = models.FloatField()
    monthly_instalments = models.IntegerField()
    monthly_instalment_amount = models.FloatField()
    quarterly_instalments = models.IntegerField()
    quarterly_instalment_amount = models.FloatField()
    halfyearly_instalments = models.IntegerField()
    halfyearly_instalment_amount = models.FloatField()
    annual_instalments = models.IntegerField()
    annual_instalment_amount = models.FloatField()
    final_payment_amount = models.FloatField()


    def __str__(self):
        return self.name