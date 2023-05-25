from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=20,blank=False)
    contra = models.CharField(max_length=30,blank=False)

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


