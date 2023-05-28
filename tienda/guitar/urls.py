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
    path('modificar-rol/<id>/',views.modificarRol,name="modificarRol"),
    path('eliminar-rol/<id>/',views.eliminarRol,name="eliminarRol"),
    path('lista-trabajadores/',views.listaTrabajadores,name="listaTrabajadores"),
    path('home-bodeguero/',views.homeBodeguero,name="homeBodeguero"),
   
]