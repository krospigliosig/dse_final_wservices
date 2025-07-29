from uuid import UUID
from datetime import date

class Postulante:
    def __init__(self, id: UUID, nombres: str, apellidos: str, dni: str,
                 email: str, fecha_nacimiento: date, estado: str):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.dni = dni
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento
        self.estado = estado