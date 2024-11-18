from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.db.models import Sum, Count,F
from django.utils import timezone
from datetime import timedelta
from django.db import models
from products.models import Product
 
from sales.models import Sale


from django.http import JsonResponse
from django.views.decorators.http import require_POST
import logging
from django.db import transaction
from django.views.decorators.http import require_GET

@require_GET
def refresh_session(request):
    if request.user.is_authenticated:
        request.session.modified = True
    return JsonResponse({'status': 'ok'})

@login_required
def dashboard(request):
    # Sales analytics
    user_products=  Product.objects.filter(user=request.user)
    user_sales=Sale.objects.filter(user=request.user)
    
    today = timezone.now().date()
    last_30_days = today - timedelta(days=30)
    
    total_sales = Sale.objects.filter(date__gte=last_30_days).aggregate(
        total=Sum('total_price'))['total'] or 0
    
    sales_by_category = Sale.objects.filter(date__gte=last_30_days).values(
        'product__category__name').annotate(
        total=Sum('total_price')).order_by('-total')
    
   
    low_stock_products = Product.objects.filter(stock__lte=F('low_stock_threshold'))

    context = {
        'total_sales': total_sales,
        'sales_by_category': sales_by_category,
        'low_stock_products': low_stock_products,
         'products':user_products,
        'sales':user_sales
    }
    return render(request, 'dashboard/dashboard.html', context)
