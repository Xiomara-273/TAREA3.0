# 1. Usar una imagen oficial liviana de Python
FROM python:3.10-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar todo el código de nuestra app al contenedor
COPY . .

# 5. Comando por defecto al iniciar el contenedor Docker
CMD ["python", "app.py"]