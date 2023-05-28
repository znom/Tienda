from typing import Any, Dict
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto, Trabajador,Invitado


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']




class productoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'


class asignarRolForm(forms.ModelForm):

    class Meta:
        model = Trabajador
        fields = ['user','rol']

class compraForm(forms.ModelForm):

    
    class Meta:
        model = Invitado
        fields = '__all__'




   





    

    

    


        
 
   