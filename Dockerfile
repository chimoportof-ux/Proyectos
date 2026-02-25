# Dockerfile para Django + WhiteNoise en Render (opción 2)

# Usa una imagen base oficial de Python
FROM python:3.11

# Directorio de trabajo dentro del contenedor
WORKDIR /code

# Copia el archivo de requisitos e instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código del proyecto
COPY . /code/

# Comando por defecto: recopila estáticos y luego inicia Gunicorn
CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn blogDataModel.wsgi:application --bind 0.0.0.0:$PORT"]