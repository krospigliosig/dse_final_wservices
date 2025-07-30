from django.db import models

class PagoModel(models.Model):
    dni = models.CharField(max_length=20)
    monto = models.FloatField()
    servicio = models.CharField(max_length=100)
    estado_transaccion = models.BooleanField()

    def __str__(self):
        return f"Pago de {self.dni} - {self.servicio} - {'Aprobado' if self.estado_transaccion else 'Rechazado'}"
