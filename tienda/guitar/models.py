from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    usuario = models.CharField(max_length=20,blank=False)
    contra = models.CharField(max_length=30,blank=False)
    contra2 = models.CharField(max_length=30,blank=False, null=True)
    email = models.CharField(max_length=30,blank=False, null=True)


    def __str__(self):
        return self.usuario

class Categoria(models.Model):
    categoria = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.categoria


class Producto(models.Model):
    nombre = models.CharField(max_length=45)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos",null=True)

    def __str__(self):
        return self.nombre
    
class Rol(models.Model):

    roles_choices = [
        ("E","Estandar"),
        ("V","Vendedor"),
        ("B","Bodeguero")
    ]

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    rol = models.CharField(max_length=1,choices=roles_choices,default="E")

    def __str__(self):
        return f'{self.user.username} posee rol {self.rol}'


