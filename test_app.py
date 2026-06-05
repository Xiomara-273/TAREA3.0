from app import app

def test_homepage_loads_successfully():
    # Crear un cliente de pruebas virtual para simular el navegador
    client = app.test_client()
    
    # Hacer una petición a la página principal
    response = client.get('/')
    
    # Validar que el servidor web responda con éxito (Código 200 OK)
    assert response.status_code == 200
    # Validar que el HTML contenga el título correcto
    assert b"Lista de Tareas" in response.data