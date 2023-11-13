from django.http import HttpResponseBadRequest
from rest_framework.response import Response
from .models import customer_data, customer_register
from .serializers import customer_data_serializer,customer_register_serializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate

# Create your views here.

class customers(APIView):
   def get(self, request):
      user_object = customer_data.objects.all()
      serializer = customer_data_serializer(user_object, many =True)
      return Response(serializer.data)
   
   def post(self , request):
         data = request.data
         print(data)
         serializer = customer_register_serializer(data=data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data)
        

