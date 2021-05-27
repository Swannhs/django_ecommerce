from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from customer.models import BasicInfo
from customer.serializer import CustomerInfoSerializer


@api_view(['GET'])
def getCustomers(request):
    customers = BasicInfo.objects.all()
    serializer = CustomerInfoSerializer(customers)
    return Response(serializer.data)
