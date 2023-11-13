from django.urls import path
from . import views 

urlpatterns = [
    path('allcustomer/', views.customers.as_view()),
]
