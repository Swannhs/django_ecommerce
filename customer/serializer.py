from rest_framework import serializers

from customer.models import BasicInfo


class CustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInfo
        fields = '__all__'
