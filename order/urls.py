from django.urls import path

from order import views

urlpatterns = [
    path('', views.getOrders, name='Orders'),
    path('item/', views.getOrderItems, name='OrderedItem'),
]
