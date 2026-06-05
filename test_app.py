import sys
import os

# Forzar a Python a buscar el archivo app.py en la raíz actual
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import app

def test_homepage_loads_successfully():
    # Crear un cliente de pruebas virtual para simular el navegador
    client = app.test_client()
    
    # Hacer una petición a la página principal
    response = client.get('/')
    
    # Validar que el servidor web responda con éxito (Código 200 OK)
    assert response.status_code == 200
    # Validar que el HTML contenga el título de tu lista
    assert b"Lista de Tareas" in response.data