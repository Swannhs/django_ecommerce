from django.urls import path

from customer import views

urlpatterns = [
    path('', views.getCustomers, name='Customer'),
]
