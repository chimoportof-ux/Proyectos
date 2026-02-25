# Usa una imagen base oficial de Python
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /code

# Copia los requisitos e instala todo junto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código al contenedor
COPY . /code/

# Recopila los archivos estáticos para producción
RUN python manage.py collectstatic --noinput

# Expone el puerto para Render (opcional)
# EXPOSE 8000

# Comando por defecto para iniciar Gunicorn
CMD ["sh", "-c", "gunicorn blogDataModel.wsgi:application --bind 0.0.0.0:$PORT"]
