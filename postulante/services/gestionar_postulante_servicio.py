from uuid import uuid4
from postulante.domain.postulante import Postulante
from postulante.repositories.implementacion.postulante_repositorio_impl import PostulanteRepositorioImpl

class GestionarPostulanteServicio:
    def __init__(self):
        self.repositorio = PostulanteRepositorioImpl()

    def crear_postulante(self, datos: dict, archivo_documento):
        postulante = Postulante(
            id=uuid4(),
            nombres=datos["nombres"],
            apellidos=datos["apellidos"],
            dni=datos["dni"],
            email=datos["email"],
            archivo_documento=str(archivo_documento),  
            estado="PENDIENTE"
        )
        self.repositorio.guardar(postulante, archivo_documento)
        return postulante
