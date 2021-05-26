from django.urls import path

from product import views

urlpatterns = [
    path('', views.getProducts, name='Products'),
]
