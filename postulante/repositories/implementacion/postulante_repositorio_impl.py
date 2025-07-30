from postulante.repositories.interface.postulante_repositorio import IPostulanteRepositorio
from postulante.domain.postulante import Postulante
from postulante.infraestructura.models.postulante_model import PostulanteModel

class PostulanteRepositorioImpl(IPostulanteRepositorio):
    def guardar(self, postulante: Postulante, archivo_documento: object) -> None:
        PostulanteModel.objects.create(
            id=postulante.id,
            nombres=postulante.nombres,
            apellidos=postulante.apellidos,
            dni=postulante.dni,
            email=postulante.email,
            archivo_documento=archivo_documento,
            estado=postulante.estado
        )

    def obtener_por_id(self, id):
        modelo = PostulanteModel.objects.get(id=id)
        return Postulante(
            id=modelo.id,
            nombres=modelo.nombres,
            apellidos=modelo.apellidos,
            dni=modelo.dni,
            email=modelo.email,
            archivo_documento=str(modelo.archivo_documento),  
            estado=modelo.estado
        )
