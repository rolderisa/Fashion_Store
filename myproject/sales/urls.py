from django.urls import path
from . import views

urlpatterns = [
    path('', views.sale_list, name='sale_list'),
    path('add/', views.add_sale, name='add_sale'),
       path('api/sales/<int:sale_id>/', views.delete_sale, name='delete_sale'),
]
