from abc import ABC, abstractmethod
from uuid import UUID
from postulante.domain.postulante import Postulante

class IPostulanteRepositorio(ABC):
    @abstractmethod
    def guardar(self, postulante: Postulante, archivo_documento: object) -> None:
        pass

    @abstractmethod
    def obtener_por_id(self, id: UUID) -> Postulante:
        pass
