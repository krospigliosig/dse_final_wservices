from django.db import models

class TransaccionBancariaModel(models.Model):
    id_transaccion = models.CharField(primary_key=True, max_length=50)
    fecha = models.DateTimeField()
    banco = models.CharField(max_length=100)
    monto = models.FloatField()

    def __str__(self):
        return f"{self.id_transaccion} - {self.banco} - {self.monto}"