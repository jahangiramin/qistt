from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('cart/', views.cart, name = 'cart'),
    path('checkout/', views.checkout, name='checkout'),
]