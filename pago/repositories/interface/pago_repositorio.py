from abc import ABC, abstractmethod
from uuid import UUID
from pago.domain.pago import Pago

class IPagoRepositorio(ABC):
    @abstractmethod
    def guardar(self, pago: Pago) -> None:
        pass

    @abstractmethod
    def obtener_por_id(self, id: UUID) -> Pago:
        pass