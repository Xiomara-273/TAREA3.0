# Tarea 3.0 - Automatización de CI/CD con GitHub Actions y Docker

## 👤 Información del Estudiante
* **Nombre:** Xiomara Scarleth Méndez Arce
* **Carrera:** Tecnología en Desarrollo de Software
* **Asignatura:** DevOps
* **Nivel / Curso:** 5to Semestre - Paralelo "5B"
* **Aplicación Entregable:** `ejercicio:3.0.0` (Sistema de Gestión de Tareas Atómicas)

---

## 🚀 Descripción del Proyecto
Este repositorio contiene una aplicación modular desarrollada en Python que simula una lista de tareas (`TodoList`), diseñada específicamente para demostrar la implementación práctica de un pipeline de **Integración Continua (CI)** y **Entrega Continua (CD)**. 

El proyecto integra pruebas unitarias automatizadas con `pytest`, empaquetamiento inmutable mediante contenedores **Docker** y la automatización completa del ciclo de vida del software usando **GitHub Actions**, publicando el artefacto final en el **GitHub Container Registry (GHCR)**.

---

## 🛠️ Arquitectura de Automatización (Flujo CI/CD)

El flujo de trabajo configurado en `.github/workflows/python-application.yml` se dispara automáticamente ante cualquier evento de `push` o `pull_request` en la rama `main`, ejecutando los siguientes bloques de control en un servidor virtual efímero (`ubuntu-latest`):

1. **Checkout:** Descarga el código fuente actualizado del repositorio.
2. **Setup Environment:** Inicializa y configura el entorno con Python 3.10.
3. **Install Dependencies:** Instala las herramientas necesarias especificadas en `requirements.txt` (incluyendo `pytest`).
4. **Automated Testing:** Ejecuta las pruebas unitarias para validar que la lógica del negocio no se haya roto.
5. **Execution Verification:** Corre la aplicación en el entorno de pruebas para verificar su salida por consola.
6. **Simulation Stage:** Simula la fase de validación de despliegue continuo (*Staging environment*).
7. **Registry Authentication:** Inicia sesión de forma segura en `ghcr.io` utilizando los permisos criptográficos nativos (`GITHUB_TOKEN`).
8. **Docker Build & Push:** Construye la imagen del contenedor basándose en el `Dockerfile` y la publica en la nube con la etiqueta oficial requerida.

---

## 📂 Estructura del Repositorio
```text
Tarea3.0/
├── .github/
│   └── workflows/
│       └── python-application.yml  # Cerebro de automatización CI/CD
├── app.py                         # Código fuente de la aplicación (Lista de tareas)
├── test_app.py                    # Suite de pruebas unitarias automatizadas
├── requirements.txt               # Manifiesto de dependencias de Python
├── Dockerfile                     # Instrucciones de compilación del contenedor Docker
└── README.md                      # Documentación técnica del proyecto (Este archivo)