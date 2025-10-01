# Dockerfile

# 1. Usar una imagen base oficial de Python.
# python:3.9-slim es una versión ligera, ideal para producción.
FROM python:3.9-slim

# 2. Establecer el directorio de trabajo dentro del contenedor.
WORKDIR /app

# 3. Copiar el archivo de requerimientos PRIMERO.
# Esto aprovecha el caché de Docker. Si requirements.txt no cambia,
# no se volverán a instalar las dependencias en futuras construcciones.
COPY requirements.txt .

# 4. Instalar las dependencias del proyecto.
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto de los archivos de la aplicación al directorio de trabajo.
COPY . .

# 6. Exponer el puerto en el que la aplicación se ejecutará.
EXPOSE 5000

# 7. Definir el comando para ejecutar la aplicación cuando se inicie el contenedor.
CMD ["python", "app.py"]