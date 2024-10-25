from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_preference, name='customer_preference'),
]
