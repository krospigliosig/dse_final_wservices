from uuid import UUID


class Postulante:
    def __init__(self, id: UUID, nombres: str, apellidos: str, dni: str,
                 email: str, archivo_documento: str, estado: str):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.dni = dni
        self.email = email
        self.archivo_documento = archivo_documento
        self.estado = estado