from celery import shared_task 

@shared_task
def tarea_hola():
    print("¡Hola desde Celery!")
    return "hola de nuevo desde Celery"