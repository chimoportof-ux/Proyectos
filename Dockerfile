# Usa Python 3.11
FROM python:3.11

WORKDIR /code

# Copia y instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn whitenoise

# Copia todo el proyecto
COPY . /code/

EXPOSE 8000

# CMD: primero collectstatic, luego gunicorn
CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn blogDataModel.wsgi:application --bind 0.0.0.0:8000"]