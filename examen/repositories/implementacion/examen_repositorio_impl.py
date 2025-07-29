from examen.repositories.interface.examen_repositorio import ExamenRepositorio
from examen.domain.examen import Examen
from examen.infraestructura.models.examen_model import ExamenModel
from postulante.infraestructura.models.postulante_model import PostulanteModel

class ExamenRepositorioImpl(ExamenRepositorio):
    def guardar(self, examen: Examen) -> None:
        postulante = PostulanteModel.objects.get(id=examen.postulante_id)
        ExamenModel.objects.create(
            id=examen.id,
            postulante=postulante,
            fecha=examen.fecha,
            estado=examen.estado,
            resultado_puntaje=examen.resultado.puntaje,
            resultado_aprobado=examen.resultado.aprobado,
            resultado_comentario=examen.resultado.comentario,
            resultado_fecha_publicacion=examen.resultado.fecha_publicacion
        )
