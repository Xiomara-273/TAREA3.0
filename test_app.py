from app import TodoList

def test_add_task_successfully():
    # Instanciar la clase de la aplicación
    todo = TodoList()
    
    # Ejecutar la acción de prueba
    result = todo.add_task("Aprender Docker y CI/CD")
    
    # Validaciones obligatorias (Asserts)
    assert result is True
    assert len(todo.get_tasks()) == 1
    assert todo.get_tasks()[0] == "Aprender Docker y CI/CD"