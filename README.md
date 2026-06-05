# Tarea 3.0 - Automatización de CI/CD con GitHub Actions y Docker

## 👤 Información del Estudiante
* **Nombre:** Xiomara Scarleth Méndez Arce
* **Semestre:** 5to Semestre
* **Paralelo:** "5B"
* **Asignatura:** DevOps / Despliegue de Aplicaciones

---

## 📝 Descripción del Proyecto
Este proyecto consiste en una aplicación web interactiva de **Lista de Tareas (To-Do List)** desarrollada en Python utilizando el microframework **Flask**. El objetivo principal de la práctica es implementar un pipeline completo de Integración y Despliegue Continuo (CI/CD) automatizado mediante **GitHub Actions** y la contenedorización de la aplicación utilizando **Docker**.

---

## ⚙️ Explicación del Funcionamiento Automatizado (CI/CD)

El archivo de configuración `.github/workflows/python-application.yml` gestiona todo el ciclo de vida del código de manera automática cada vez que se realiza un `git push` a la rama `main`. El funcionamiento se divide en las siguientes etapas clave:

1. **Entorno de Pruebas (CI):**
   * Se levanta un servidor virtual limpio basado en `ubuntu-latest`.
   * Se instala la versión de **Python 3.10** y se configuran las dependencias del archivo `requirements.txt` (Flask y Pytest).
   * Se ejecutan de forma aislada las pruebas unitarias automatizadas con **Pytest** para verificar que el servidor web responda correctamente (Código HTTP 200 OK) y que no existan errores de sintaxis en `app.py`.

2. **Empaquetado y Publicación (CD):**
   * Una vez que las pruebas pasan con éxito (**Check Verde ✅**), el pipeline se autentica de forma segura en el registro de contenedores de GitHub (**GHCR**).
   * Se lee el archivo `Dockerfile` para empaquetar la aplicación web en una imagen ligera de Docker.
   * Finalmente, la imagen se publica automáticamente en GitHub Packages bajo la nomenclatura oficial: `ghcr.io/xiomara-273/ejercicio:3.0.0`.

---

## 🐳 Instrucciones de Ejecución Local (Docker)

Para descargar y ejecutar esta aplicación web interactiva en cualquier computadora local que disponga de Docker, ejecute los siguientes comandos en su terminal:

```bash
# 1. Descargar la imagen pública desde el registro de GitHub
docker pull ghcr.io/xiomara-273/ejercicio:3.0.0

# 2. Desplegar el contenedor mapeando el puerto web
docker run -d -p 5000:5000 --name mi_app_web ghcr.io/xiomara-273/ejercicio:3.0.0