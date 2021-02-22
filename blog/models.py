from django.db import models

class Placas (models.Model):
    nombre = models.CharField(max_length=50)
    chasis = models.CharField(max_length=15)
    no_Cedula = models.CharField(max_length=15)
    noPlaca = models.CharField(max_length=20, blank=True)
    compania = models.CharField(max_length=50,blank=True)
    fechaOrden = models.CharField(max_length=20, blank=True)
    endoso = models.CharField(max_length=20, blank=True)
    FechaEndoso = models.CharField(max_length=20, blank=True)
    Estado = [
         ('Pendiente de Placa', 'Pendiente de Placa'),
        ('placa y matricula', 'placa y matricula'),
        ('placa y copia M.', 'placa y copia M.'),
        ('placa entregada', 'placa entregada'),
        ('Endosando', 'Endosando'),
        ('Matricula Lista', 'Matricula Lista'),
        ('placa y M. Entregada', 'placa y M. Entregada'),

    ]
    Estado = models.CharField(
        max_length=22,
        choices=Estado,
        default=None,
    )

    fecha =  models.DateTimeField(auto_now_add=True)
    cedula = models.BooleanField(default=True)
    Comentario=models.TextField(max_length=50)
