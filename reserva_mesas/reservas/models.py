from django.db import models

class mesa(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    # Pizarra: Num Mesa -> Integer
    numero_mesa = models.IntegerField() 
    
    # Pizarra: Ubicación -> String
    ubicacion = models.CharField(max_length=150)
    
    # Pizarra: Num Sillas -> Integer
    numero_sillas = models.IntegerField() 
    
    # Pizarra: Disponible -> Booleano
    disponible = models.BooleanField(default=True) 
    
    def __str__(self):
        # ⚠️ IMPORTANTE: Como numero_mesa ahora es un entero, 
        # hay que convertirlo a string para que Django no de error.
        return str(self.numero_mesa)
