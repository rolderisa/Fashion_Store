from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('refresh-session/', views.refresh_session, name='refresh_session'),
    path('storefront/', views.storefront, name='storefront'),
]
