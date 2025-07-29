from uuid import UUID
from datetime import datetime
from .resultado_examen import ResultadoExamen

class Examen:
    def __init__(self, id: UUID, postulante_id: UUID, fecha: datetime, estado: str = "CERRADO",
                 resultado: ResultadoExamen | None = None):
        self.id = id
        self.postulante_id = postulante_id
        self.fecha = fecha
        self.estado = estado  
        self.resultado = resultado or ResultadoExamen()

    def fijar_resultado(self, puntaje: float, comentario: str = ""):
        self.resultado.puntaje = puntaje
        self.resultado.aprobado = self.resultado.es_aprobado()
        self.resultado.comentario = comentario
        self.resultado.fecha_publicacion = datetime.now()

    def cerrar(self):
        self.estado = "CERRADO"
