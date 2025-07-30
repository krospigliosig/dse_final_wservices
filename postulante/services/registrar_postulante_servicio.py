from postulante.infraestructura.models.postulante_model import PostulanteModel

def registrar_postulante(data):
    return PostulanteModel.objects.create(**data)
