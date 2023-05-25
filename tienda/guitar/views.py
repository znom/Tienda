from django.shortcuts import render,redirect
from .models import Producto
from .forms import UserRegisterForm
from django.contrib import messages




def home(request):


    productos = Producto.objects.all()
    context = {'productos':productos}
    return render(request, 'guitar/home.html',context)



def registro(request):
    
    if request.method == 'POST':
       form = UserRegisterForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('home')
    else:
        form = UserRegisterForm()


        

    context = {'form':form }

    
        
    return render(request,'guitar/registro.html',context) 



