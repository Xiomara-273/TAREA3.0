from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# Base de datos temporal en memoria
tasks = ["Configurar Dockerfile", "Implementar GitHub Actions", "Ver mi app en el navegador"]

# Diseño HTML simple incrustado para no crear más archivos
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Tarea 3.0 - DevOps</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f9; margin: 40px; color: #333; }
        .container { max-width: 500px; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        h2 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
        ul { list-style: none; padding: 0; }
        li { background: #eee; margin: 5px 0; padding: 10px; border-radius: 4px; display: flex; justify-content: space-between; }
        input[type="text"] { width: 70%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
        button { padding: 8px 15px; background: #3498db; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #2980b9; }
    </style>
</head>
<body>
    <div class="container">
        <h2>📝 Lista de Tareas de Xiomara (5B)</h2>
        <ul>
            {% for task in tasks %}
                <li>{{ task }}</li>
            {% endfor %}
        </ul>
        <form action="/add" method="POST">
            <input type="text" name="task" placeholder="Nueva tarea..." required>
            <button type="submit">Agregar</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

if __name__ == "__main__":
    # El host '0.0.0.0' es obligatorio para que Docker pueda transmitir el puerto hacia afuera
    app.run(host="0.0.0.0", port=5000)