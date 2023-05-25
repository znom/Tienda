from django import forms
from .models import Usuario

class formRegistro(forms.ModelForm):

    usuario = forms.CharField(min_length=3,max_length=20)
    email = forms.EmailField(max_length = 200)
    contra = forms.CharField(widget=forms.PasswordInput)
    contra2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = '__all__'


        
 
   