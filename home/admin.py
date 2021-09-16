from home.models import Term,Paymenttype, Category,Product, Priceplan, Priceplandetail
from django.contrib import admin

# Register your models here.

admin.site.register(Term)
admin.site.register(Paymenttype)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Priceplan)
admin.site.register(Priceplandetail)