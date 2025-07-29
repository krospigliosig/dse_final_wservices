import uuid
from datetime import datetime
from examen.domain.examen import Examen
from examen.domain.resultado_examen import ResultadoExamen
from examen.repositories.interface.examen_repositorio import ExamenRepositorio

class RegistrarExamenServicio:
    def __init__(self, repo: ExamenRepositorio):
        self.repo = repo

    def ejecutar(self, dni: str, puntaje: float, comentario: str = ""):
        from postulante.infraestructura.models.postulante_model import PostulanteModel

        postulante = PostulanteModel.objects.get(dni=dni)
        examen = Examen(id=uuid.uuid4(), postulante_id=postulante.id, fecha=datetime.now())
        examen.fijar_resultado(puntaje, comentario)
        examen.cerrar()
        self.repo.guardar(examen)
