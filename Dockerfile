# Usamos una imagen oficial de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de los archivos
COPY . .

# Definimos el comando por defecto para correr el script
CMD ["python", "scraper.py"]
