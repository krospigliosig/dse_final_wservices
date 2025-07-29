from abc import ABC, abstractmethod
from examen.domain.examen import Examen

class ExamenRepositorio(ABC):
    @abstractmethod
    def guardar(self, examen: Examen) -> None:
        pass
