from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.db.models import Sum, Count,F
from django.utils import timezone
from datetime import timedelta
from django.db import models
from .models import Product,Cart,CartItem

from django.http import JsonResponse
from django.views.decorators.http import require_POST
import logging
from django.db import transaction



logger = logging.getLogger(__name__)
@require_POST
@login_required
def add_to_cart(request, product_id):
    try:
        with transaction.atomic():
            product = Product.objects.get(id=product_id)
            cart, _ = Cart.objects.get_or_create(user=request.user)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            
            if not created:
                cart_item.quantity += 1
                cart_item.save()

            cart_count = sum(item.quantity for item in cart.cartitem_set.all())

        return JsonResponse({
            'status': 'success',
            'message': 'Item added to cart',
            'cart_count': cart_count
        })
    except Product.DoesNotExist:
        logger.error(f"Product with id {product_id} not found")
        return JsonResponse({
            'status': 'error',
            'message': 'Product not found'
        }, status=404)
    except Exception as e:
        logger.error(f"Error adding product {product_id} to cart: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': 'An unexpected error occurred'
        }, status=500)
# @login_required
# def view_cart(request):
#     cart,created=Cart.objects.get_or_create(user=request.user)
#     items=cart.items.all()
#     total=sum(item.product.price * item.quantity for item in items)
#     return render(request, 'store/cart.html',{'items':items,'total':total})    
@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total = sum(item.product.price * item.quantity for item in items)
    return render(request, 'cart/cart.html', {'items': items, 'total': total})