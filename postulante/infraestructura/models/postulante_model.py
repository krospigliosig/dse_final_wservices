
from django.db import models
import uuid

class PostulanteModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
