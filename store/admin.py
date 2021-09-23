from store.models import Category, Priceplan, Product, Term
from django.contrib import admin

# Register your models here.

admin.site.register(Term)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Priceplan)