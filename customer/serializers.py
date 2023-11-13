from rest_framework import serializers
from .models import *


class customer_data_serializer(serializers.ModelSerializer):
    class Meta:
        model = customer_data
        fields = ['id', 'name', 'address']
        
class customer_register_serializer(serializers.ModelSerializer):
    class Meta:
        model = customer_register
        fields = '__all__'
    