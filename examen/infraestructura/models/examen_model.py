from django.db import models
import uuid
from postulante.infraestructura.models.postulante_model import PostulanteModel

class ExamenModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    postulante = models.ForeignKey(PostulanteModel, on_delete=models.CASCADE, related_name="examenes")
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[("PROGRAMADO", "PROGRAMADO"), ("EN_PROCESO", "EN_PROCESO"), ("CERRADO", "CERRADO")],
        default="CERRADO"
    )
    resultado_puntaje = models.FloatField()
    resultado_aprobado = models.BooleanField()
    resultado_comentario = models.TextField(blank=True, default="")
    resultado_fecha_publicacion = models.DateTimeField(auto_now_add=True)
