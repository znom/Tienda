from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('registro/',views.registro,name="registro"),

    path('lista-productos/',views.listaProductos,name="listaProductos"),
    path('agregar-productos/',views.agregarProductos,name="agregarProductos"),
    path('modificar-producto/<id>/',views.modificarProducto,name="modificarProducto"),
    path('eliminar-producto/<id>/',views.eliminarProducto,name="eliminarProducto"),
    path('asignar-roles/',views.asignarRoles,name="asignarRoles"),
    path('lista-trabajadores/',views.listaTrabajadores,name="listaTrabajadores"),
   
]