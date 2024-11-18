from django.urls import path
from . import views

urlpatterns = [
    path('', views.sale_list, name='sale_list'),
    path('add/', views.add_sale, name='add_sale'),
    path('refresh-session/', views.refresh_session, name='refresh_session'),
       path('api/sales/<int:sale_id>/', views.delete_sale, name='delete_sale'),
]
