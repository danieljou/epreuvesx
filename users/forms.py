from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('photo','is_admin','is_professeur','username','last_name','first_name','password1','password2')


class UserUpadateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('photo','is_admin','is_professeur','username','last_name','first_name')



class UserAccount(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('photo','username','last_name','first_name', 'password1','password2')
