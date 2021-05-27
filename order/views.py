from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from order.models import Order, OrderItem
from order.serializers import OrderSerializer, OrderItemSerializer


@api_view(['GET'])
def getOrders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getOrderItems(request):
    items = OrderItem.objects.all()
    serializer = OrderItemSerializer(items, many=True)
    return Response(serializer.data)
