from uuid import uuid4
from datetime import datetime
from examen.domain.examen import Examen
from examen.repositories.implementacion.examen_repositorio_impl import ExamenRepositorioImpl
from pago.infraestructura.models.pago_model import PagoModel

class ProgramarExamenServicio:
    def __init__(self):
        self.repo = ExamenRepositorioImpl()

    def programar(self, postulante_id, fecha: datetime) -> Examen:
        if not PagoModel.objects.filter(postulante_id=postulante_id, estado="APROBADO").exists():
            raise ValueError("El postulante no tiene pago aprobado.")
        exam = Examen(
            id=uuid4(), postulante_id=postulante_id, fecha=fecha,
            asistencia=False, respuestas={}, estado="PROGRAMADO"
        )
        self.repo.guardar(exam)
        return exam
