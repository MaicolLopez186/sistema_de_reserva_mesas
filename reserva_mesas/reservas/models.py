from django.db import models

class mesa(models.Model):
   id_mesa = models.AutoField(primary_key=True)
   numero_mesa = models.CharField(max_length=200)
   ubicacion= models.CharField(max_length=150)
   numero_sillas= models.CharField(max_length=150)
   disponible= models.CharField(max_length=150)  
    

   def __str__(self):
       return self.numero_mesa

class cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre