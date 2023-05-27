from django.shortcuts import render,redirect,get_object_or_404
from .models import Producto, User, Trabajador
from .forms import CustomUserCreationForm,productoForm,asignarRolForm
from django.contrib import messages
from django.contrib.auth import authenticate, login




def home(request):

    productos = Producto.objects.all()
    context = {'productos':productos}
    return render(request, 'guitar/home.html',context)


def registro(request):
    data = {
        'form':CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect('home')
        data['form'] = formulario


    return render(request,'registration/registro.html',data) 


def listaProductos(request):
    productos = Producto.objects.all()
    context = {'productos':productos}
    return render(request, 'guitar/vistaAdmin/listaProductos.html', context)

def agregarProductos(request):

    data ={
        'form':productoForm
    }

    if request.method == 'POST':
        formulario = productoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Agregado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'guitar/vistaAdmin/agregarProductos.html',data)

def modificarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)

    data = {
        'form':productoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = productoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('listaProductos')
        
        data["form"] = formulario

    return render(request, 'guitar/vistaAdmin/modificarProducto.html',data)


def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('listaProductos')


def asignarRoles(request):
    
    data = {
        'form':asignarRolForm
    }

    if request.method == 'POST':
        formulario = asignarRolForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
          
            return redirect('listaTrabajadores')
        data['form'] = formulario

    return render(request, 'guitar/vistaAdmin/asignarRoles.html',data)

def listaTrabajadores(request):
    trabajadores = Trabajador.objects.all()
    
    context = {'trabajadores':trabajadores}
    

    return render(request,'guitar/vistaAdmin/listaTrabajadores.html',context)



