from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from . models import Customer
from django.forms import ModelForm,widgets
from django import forms

class CustomUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','city','pincode','state','mobileno']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pincode':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),   
            'mobileno':forms.NumberInput(attrs={'class':'form-control'}),
        }

class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label='Old password',widget=forms.PasswordInput(attrs={'autofocus':'True','autocomplete':'current-password','class':'form-control'}))
    new_password1=forms.CharField(label='New password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2=forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))