from django.shortcuts import render,redirect
from .models import Producto
from .forms import formRegistro
from django.contrib import messages



def home(request):

    productos = Producto.objects.all()
    context = {'productos':productos}
    return render(request, 'guitar/home.html',context)



def registro(request):
    
    if request.method =='POST':
        form = formRegistro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = formRegistro()

    context1 = {'form':form}
        
    return render(request,'guitar/registro.html',context1) 



