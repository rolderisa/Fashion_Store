from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.db.models import Sum, Count,F
from django.utils import timezone
from datetime import timedelta
from django.db import models
from .models import Sale
from .forms import SaleForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import logging
from django.views.decorators.http import require_http_methods
from django.db import transaction
from django.views.decorators.http import require_GET

@require_GET
def refresh_session(request):
    if request.user.is_authenticated:
        request.session.modified = True
    return JsonResponse({'status': 'ok'})
@login_required
def sale_list(request):
    # sales = Sale.objects.all()
    sales=Sale.objects.filter(user=request.user)

    return render(request, 'sales/sale_list.html', {'sales': sales})


@login_required
def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.user = request.user
            sale.save()
            
            # Update product stock
            product = sale.product
            product.stock -= sale.quantity
            product.save()
            
            return redirect('sale_list')
    else:
        form = SaleForm()
    return render(request, 'sales/add_sale.html', {'form': form})

@require_http_methods(["DELETE"])
def delete_sale(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    sale.delete()
    return JsonResponse({"message": "Sale deleted successfully"}, status=200)    