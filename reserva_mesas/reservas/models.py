from django.db import models

class mesa(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    numero_mesa = models.IntegerField()
    ubicacion = models.CharField(max_length=150)
    numero_sillas = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Mesa {self.numero_mesa}"