from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.db.models import Sum, Count,F
from django.utils import timezone
from datetime import timedelta
from django.db import models
from .models import Product,  Category
from .forms import ProductForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import logging
from django.db import transaction
from django.contrib import messages


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


# @login_required
# def add_product(request):
#     # Check if there are any categories, if not, create default ones
#     if Category.objects.count() == 0:
#         Category.objects.create(name="Men's Clothing", gender='M')
#         Category.objects.create(name="Women's Clothing", gender='W')
#         Category.objects.create(name="Accessories", gender='U')  # Unisex category

#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             if 'image' in request.FILES:
#                 product.image = request.FILES['image']
#             product.save()
#             messages.success(request, 'Product added successfully!')
#             return redirect('product_list')
#         else:
#             messages.error(request, 'Error adding product. Please check the form.')
#     else:
#         form = ProductForm()
    
#     return render(request, 'products/add_product.html', {'form': form})

@login_required
def add_product(request):
    if Category.objects.count() == 0:
        Category.objects.create(name="Men's Clothing", gender='M')
        Category.objects.create(name="Women's Clothing", gender='W')
        Category.objects.create(name="Accessories", gender='U')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            if 'image' in request.FILES:
                product.image = request.FILES['image']
            product.save()
            messages.success(request, 'Product added successfully!')
            return redirect('product_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = ProductForm()
    
    return render(request, 'products/add_product.html', {'form': form})

def storefront(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
    
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'products/storefront.html', context)

