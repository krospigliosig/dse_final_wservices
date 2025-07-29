from datetime import datetime

class ResultadoExamen:
    def __init__(self, puntaje: float = 0.0, aprobado: bool = False, comentario: str = "", fecha_publicacion: datetime = None):
        self.puntaje = puntaje
        self.aprobado = aprobado
        self.comentario = comentario
        self.fecha_publicacion = fecha_publicacion or datetime.now()

    def es_aprobado(self) -> bool:
        return self.puntaje >= 10.0
