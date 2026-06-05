class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task:
            return False
        self.tasks.append(task)
        return True

    def get_tasks(self):
        return self.tasks

if __name__ == "__main__":
    print("--- Ejecutando Aplicación: Lista de Tareas 3.0 ---")
    my_list = TodoList()
    my_list.add_task("Configurar Dockerfile")
    my_list.add_task("Implementar GitHub Actions")
    print(f"Tareas actuales en la lista: {my_list.get_tasks()}")