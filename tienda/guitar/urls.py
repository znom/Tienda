from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('registro/',views.registro,name="registro"),

    path('home-admin/',views.homeAdmin,name="homeAdmin"),
    path('agregar-productos/',views.agregarProductos,name="agregarProductos"),
    path('modificar-producto/<id>/',views.modificarProducto,name="modificarProducto"),
    path('eliminar-producto/<id>/',views.eliminarProducto,name="eliminarProducto"),
   
]