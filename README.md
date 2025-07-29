# Servicios Web – UNSA BPM Integración

### Nombre del equipo: Los malditos del BPMN

#### Integrantes:
- Salim Adrián Jorge Rodriguez
- Kerin Sebastián Larico Huillca
- Kristopher Rospigliosi Gonzales

---

### Propósito del Proyecto
Desarrollar servicios web RESTful en Django para dar soporte a los procesos modelados en BonitaSoft, facilitando operaciones automatizadas de matrícula, admisión y contratación docente. Estos servicios exponen una API modular, documentada bajo OpenAPI/Swagger, y estructurada con principios de **Domain-driven Design (DDD)**.

---

### Visión General de la Arquitectura: DDD

El sistema ha sido diseñado aplicando los principios de **Domain-driven Design**, separando el sistema en **Bounded Contexts** claramente definidos:

- `Matrícula`: lógica para verificación de pagos, prerrequisitos y registro.
- `Admisión`: gestión de postulantes, validación de documentos, y publicación de resultados.
- `Contratación`: registro, evaluación y contratación de profesores.

Cada módulo representa un subdominio, con sus propias entidades, reglas de negocio y servicios REST. Se ha usado una estructura por capas (infraestructura, dominio y aplicación), facilitando la escalabilidad, mantenibilidad y pruebas.

---

### Servicios REST y funcionalidades (OpenAPI + Swagger)

Los siguientes módulos están implementados como microservicios REST, documentados con Swagger.

---

#### Módulo: Matrícula <Gestión de Registro de Cursos>
**Propósito:** Validar pagos y prerrequisitos para registrar al estudiante.

##### Endpoints:
- `GET /api/matricula/cronograma`  
  *Obtiene las fechas de matrícula y grupos habilitados.*

- `POST /api/matricula/verificar-pago`  
  **Body:** `{ "codigo_estudiante": "20211234" }`  
  *Verifica si el pago del estudiante fue realizado.*

- `POST /api/matricula/registrar`  
  **Body:** `{ "codigo_estudiante": "20211234", "cursos": ["CC101", "CC202"] }`  
  *Registra al estudiante en los cursos elegidos.*

---

#### Módulo: Admisión <Proceso de Inscripción y Evaluación>
**Propósito:** Inscribir postulantes, verificar requisitos y publicar resultados.

##### Endpoints:
- `POST /api/admision/inscribir`  
  **Body:** `{ "dni": "12345678", "carrera": "Ingeniería de Sistemas" }`  
  *Registra nuevo postulante.*

- `POST /api/admision/validar`  
  **Body:** `{ "dni": "12345678", "documentos": ["cert_nota.pdf", "dni.jpg"] }`  
  *Valida los documentos enviados.*

- `GET /api/admision/resultados?dni=12345678`  
  *Devuelve el puntaje del postulante tras la evaluación.*

---

#### Módulo: Contratación <Proceso de Selección Docente>
**Propósito:** Gestionar postulaciones y evaluación docente.

##### Endpoints:
- `POST /api/docentes/postular`  
  **Body:** `{ "nombre": "Luis Pérez", "cv": "luis_cv.pdf", "area": "Matemática" }`  
  *Envía expediente del docente postulante.*

- `GET /api/docentes/evaluar?id=12`  
  *Consulta resultados de evaluación docente.*

- `POST /api/docentes/firma`  
  **Body:** `{ "id_docente": 12, "firmado": true }`  
  *Registra la firma digital del contrato.*

---

### Documentación Swagger / OpenAPI
- Interfaz Swagger UI: [URL_SWAGGER](#)
- Archivo OpenAPI (openapi.yaml): [Descargar](#)

---

### Modelos / Entidades y Agregados Clave

#### Matrícula
- `Estudiante`: código, nombre, grupo, estado
- `Curso`: código, nombre, prerrequisitos
- `Registro`: estudiante, lista de cursos, fecha

#### Admisión
- `Postulante`: dni, carrera, estado
- `Documento`: nombre, tipo, archivo
- `Resultado`: puntaje, carrera asignada

#### Contratación
- `Docente`: nombre, área, experiencia
- `Expediente`: cv, publicaciones, certificados
- `Evaluación`: puntaje, rúbrica, comité

---

> Todos los servicios están integrados a los procesos BPMN de BonitaSoft, usando tareas automáticas y llamadas HTTP seguras.

---

### URL del repositorio
.(https://github.com/krospigliosig/dse_final_wservices.git).
