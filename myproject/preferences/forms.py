from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from .models import  CustomerPreference



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class CustomerPreferenceForm(forms.ModelForm):
    class Meta:
        model = CustomerPreference
        fields = ['favorite_category', 'size', 'color']
