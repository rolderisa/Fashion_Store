from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.db.models import Sum, Count,F
from django.utils import timezone
from datetime import timedelta
from django.db import models
from .models import  CustomerPreference
from .forms import  CustomerPreferenceForm, UserRegisterForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import logging
from django.db import transaction

# Create your views here.
@login_required
def customer_preference(request):
    preference, created = CustomerPreference.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = CustomerPreferenceForm(request.POST, instance=preference)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = CustomerPreferenceForm(instance=preference)
    
    return render(request, 'preferences/customer_preference.html', {'form': form})

