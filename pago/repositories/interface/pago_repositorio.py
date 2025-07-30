from abc import ABC, abstractmethod
from pago.domain.pago import Pago

class PagoRepositorio(ABC):

    @abstractmethod
    def guardar_pago(self, pago: Pago):
        pass

    @abstractmethod
    def obtener_pagos_por_dni(self, dni: str) -> list[Pago]:
        pass
