from uuid import uuid4
from postulante.domain.postulante import Postulante
from postulante.repositories.implementacion.postulante_repositorio_impl import PostulanteRepositorioImpl

class GestionarPostulanteServicio:
    def __init__(self):
        self.repositorio = PostulanteRepositorioImpl()

    def crear_postulante(self, datos: dict):
        postulante = Postulante(
            id=uuid4(),
            nombres=datos["nombres"],
            apellidos=datos["apellidos"],
            dni=datos["dni"],
            email=datos["email"],
            fecha_nacimiento=datos["fecha_nacimiento"],
            estado="PENDIENTE"
        )
        self.repositorio.guardar(postulante)
        return postulante
