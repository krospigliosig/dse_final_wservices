from django.db import models
import uuid
from postulante.infraestructura.models.postulante_model import PostulanteModel
from .transaccion_bancaria_model import TransaccionBancariaModel

class PagoModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    postulante = models.ForeignKey(PostulanteModel, on_delete=models.CASCADE)
    monto = models.FloatField()
    moneda = models.CharField(max_length=10)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('PENDIENTE', 'PENDIENTE'), ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO')])
    motivo_rechazo = models.TextField(blank=True, null=True)
    transaccion = models.OneToOneField(TransaccionBancariaModel, on_delete=models.SET_NULL, null=True, blank=True)