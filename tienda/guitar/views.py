from django.shortcuts import render,redirect,get_object_or_404
from .models import Producto, User, Trabajador
from .forms import CustomUserCreationForm,productoForm,asignarRolForm,compraForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from guitar.carrito import Carrito




def home(request):

    trabajador = Trabajador.objects.all()
    """ for t in trabajador:
        if t.rol == "B":
            return redirect("homeBodeguero")
        if t.rol == "V":
            return redirect("homeBodeguero")
        if t.rol != "B" and t.rol != "V" and t.rol != "E":
            return redirect("home") """
            
    productos = Producto.objects.all()
    context = {'productos':productos,'trabajador':trabajador}
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
            
            trabajador = Trabajador.objects.all()
            for t in trabajador:
                if t.rol == "B":
                    return redirect(to='homeBodeguero')
                if t.rol == "V":
                    return redirect('homeBodeguero')
                if t.rol != "B" and t.rol != "V" and t.rol != "E": 
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

def modificarRol(request, id):
    trabajador = get_object_or_404(Trabajador, id=id)

    data = {
        'form':asignarRolForm(instance=trabajador)
    }

    if request.method == 'POST':
        formulario = asignarRolForm(data=request.POST, instance=trabajador, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('listaTrabajadores')
        
        data["form"] = formulario

    return render(request, 'guitar/vistaAdmin/modificarRol.html',data)


def eliminarRol(request, id):
    trabajador = get_object_or_404(Trabajador, id=id)
    trabajador.delete()
    return redirect('listaTrabajadores')



def listaTrabajadores(request):
    trabajadores = Trabajador.objects.all()
    
    context = {'trabajadores':trabajadores}
    

    return render(request,'guitar/vistaAdmin/listaTrabajadores.html',context)



def homeBodeguero(request):

    return render(request,'guitar/vistaBodeguero/homeBodeguero.html')




# FUNCIONES DEL CARRITO DE COMPRA <33

def carrito(request):
    return render(request, "guitar/carrito.html")

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")


def formularioCompra(request):
    
    if request.user.is_authenticated:
        return redirect("home")
    else:
        data ={
        'form': compraForm
    }

    if request.method == 'POST':
        formulario = compraForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
        else:
            data["form"] = formulario

    
    

    return render(request,'guitar/formularioCompra.html',data)
